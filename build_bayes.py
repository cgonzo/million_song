#!/usr/bin/python

import common
import json
import re
import sys
import numpy
import gc

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	artist_id=track_data["artist_id"]
	if(artist_dict.has_key(artist_id)):
		if len(terms)>0:
			term_frequencies=track_data["artist_terms_freq"]
			terms=track_data["artist_terms"]
			top_term=0
			for i in range(len(terms)):
				if(term_frequencies[i]>term_frequencies[top_term]):
					top_term=i
			# if the top term is in one of the terms we care about, output it
			if term_dict.has_key(terms[top_term]):
				# build output array
				interesting_data={}
				for data_name in interesting_data_names:
					if(track_data[data_name]!=0):
						interesting_data[data_name]=track_data[data_name]
				yield(terms[top_term],json.dumps(interesting_data))

def reduce(word, counts):
	# initialize storage
	interesting_data={}
	for data_name in interesting_data_names:
		interesting_data[data_name]=[]
	mean={}
	variance={}
	# go through each song and store the data we want in interesting_data
	for count in counts:
		track_data=json.loads(count)
		for data_name in interesting_data_names:
			if(data_name in track_data.keys()):
				interesting_data[data_name].append(track_data[data_name])
	# convert lists in interesting_data to arrays and find mean and variance
	for data_name in interesting_data_names:
		data_array=numpy.array(interesting_data[data_name])
		mean[data_name]=numpy.mean(data_array,axis=0).tolist()
		variance[data_name]=numpy.var(data_array,axis=0).tolist()
	# output
	yield(word,json.dumps([len(counts),mean,variance]))
	del interesting_data
	del mean
	del variance
	gc.collect()		
		
	

if __name__ == "__main__":
	global interesting_data_names
	interesting_data_names=["duration","num_bars","variance_bar_length","num_beats",
			"variance_beats_length","danceability","end_of_fade_in","energy","key","loudness","mode",
			"num_sections","variance_sections_length","num_segments","variance_segments_length",
			"segment_loudness_max","segment_loudness_time","segment_loudness_mean",
			"segment_loudness_variance","segment_pitches_mean","segment_pitches_variance",
			"segment_timbres_mean","segment_timbres_variance","hottness","fade_out","num_tatums",
			"variance_tatums_length","tempo","time_signature","year"]
	# create dictionary of test artists
	global artist_dict
	artist_dict={}
	f = open("artists_train.txt",'r')
	for artist in f:
		artist_dict[artist.rstrip()]=1
	f.close()
	global term_dict
	term_dict={}
	f = open("artist_by_most_popular_term_sorted.txt")
	for term_line in f:
		term_line_split=re.split("\t",term_line.rstrip())
		term_dict[term_line_split[1]]=1
	f.close()
	common.main(map, reduce)
