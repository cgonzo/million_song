#!/usr/bin/python

import common
import json
import sys
import numpy
import re
import os
import glob

# input: songs (possibly to classify)
# output: categories, category_prediction_percentage
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	artist_id=track_data["artist_id"]
	# find the actual term we're looking for
	artist_terms=track_data["artist_terms"]
	if len(artist_terms)>0:
		term_frequencies=track_data["artist_terms_freq"]
		top_term=0
		for i in range(len(artist_terms)):
			if(term_frequencies[i]>term_frequencies[top_term]):
				top_term=i
		actual_term=artist_terms[top_term]	
		# we only want to do this if it's one of the categories we classify
		if actual_term == "rock":
			# make data array for this track
			data_for_key=[]
			for data_name in interesting_data_names:
				if(getattr(track_data[data_name],'__iter__',False)):
					for data in track_data[data_name]:
						data_for_key.append(data)
				else:
					data_for_key.append(track_data[data_name])
			data_for_key_array=numpy.array(data_for_key)
			# figure out which category gives us the top classifier
			top_probability_term=actual_term # initialize top term
			top_probability=-1000
			classifier_data=classifier["rock"]
			probabilities=[]
			v=numpy.array(classifier_data)
			term_probability=numpy.dot(v,data_for_key_array.T)-threshold[classifier_term]
			term_probability_string="%010.6f" %term_probability
			title=track_data["title"]
			yield(term_probability_string,title)
		
def reduce(word, counts):
	pass

if __name__ == "__main__":
	global interesting_data_names
	# removing hottness for now because it keeps us from inverting our matricies
	interesting_data_names=["duration","num_bars","variance_bar_length","num_beats",
			"variance_beats_length","danceability","end_of_fade_in","energy","key","loudness","mode",
			"num_sections","variance_sections_length","num_segments","variance_segments_length",
			"segment_loudness_max","segment_loudness_time","segment_loudness_mean",
			"segment_loudness_variance","segment_pitches_mean","segment_pitches_variance",
			"segment_timbres_mean","segment_timbres_variance","fade_out","num_tatums",
			"variance_tatums_length","tempo","time_signature","year"]
	# import our classifier
	# we want to iterate over all files starting with "part" in the directory
	# code from http://bogdan.org.ua/2007/08/12/python-iterate-and-read-all-files-in-a-directory-folder.html
	global classifier
	global threshold
	classifier={}
	threshold={}
	path = 'build_fisher/'
	for infile in glob.glob( os.path.join(path, 'part*') ):
		f = open(infile,'r')
		for classifier_line in f:
			classifier_line_split=re.split("\t",classifier_line.rstrip())
			classifier_data_split=re.split(",",classifier_line_split[1],maxsplit=1)
			threshold[classifier_line_split[0]]=float(classifier_data_split[0])
			classifier[classifier_line_split[0]]=json.loads(classifier_data_split[1])
		f.close()
	common.main(map, reduce)
