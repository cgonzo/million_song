#!/usr/bin/python

import common
import json
import re
import sys
import numpy
from numpy import linalg
import gc

# input: file name
# output: top term, data
# but only if top term is in the top 10
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	artist_id=track_data["artist_id"]
	if(artist_dict.has_key(artist_id)):
		# output array
		artist_terms=track_data["artist_terms"]
		if len(artist_terms)>0:
			term_frequencies=track_data["artist_terms_freq"]
			top_term=0
			for i in range(len(artist_terms)):
				if(term_frequencies[i]>term_frequencies[top_term]):
					top_term=i
			# if the top term is in one of the terms we care about, output it
			if term_dict.has_key(artist_terms[top_term]):
				# go from large dictionary to array of terms we care about here
				data_for_output=[]
				for data_name in interesting_data_names:
					if(getattr(track_data[data_name],'__iter__',False)):
						for data in track_data[data_name]:
							data_for_output.append(data)
					else:
						data_for_output.append(track_data[data_name])
				# and output our data
				for key in term_dict.keys():
					if key==artist_terms[top_term]:
						match_string="1,"
						yield(key,match_string+json.dumps(data_for_output))
					elif (not key in artist_terms):
						match_string="0,"
						yield(key,match_string+json.dumps(data_for_output))
				

def reduce(word, counts):
	# initialize storage
	# data_for_key
	# new row for each observation
	# column=data
	data_for_key=[]
	data_for_not_key=[]
	data_for_key_mean=[]
	data_for_not_key_mean=[]
	data_for_key_covariance=[]
	data_for_not_key_covariance=[]
	# go through each song and store the data we want in interesting_data
	for count in counts:
		count_split=re.split(",",count,maxsplit=1)
		track_data=json.loads(count_split[1])
		if count_split[0]=="1":
			data_for_key.append(track_data)
		else:
			data_for_not_key.append(track_data)
		del track_data
		gc.collect()
	data_for_key_array=numpy.array(data_for_key)
	data_for_not_key_array=numpy.array(data_for_not_key)
#	print json.dumps(data_for_key)
#	print json.dumps(data_for_not_key)
#	print numpy.shape(data_for_key)
#	print numpy.shape(data_for_not_key)
	mean1=numpy.mean(data_for_key_array,axis=0)
	mean2=numpy.mean(data_for_not_key_array,axis=0)
	#scatter1=numpy.shape(data_for_key_array)[0]*numpy.cov(data_for_key_array,rowvar=0)
	#scatter2=numpy.shape(data_for_not_key_array)[0]*numpy.cov(data_for_not_key_array,rowvar=0)
	scatter1=numpy.cov(data_for_key_array,rowvar=0)
	scatter2=numpy.cov(data_for_not_key_array,rowvar=0)
#	print numpy.shape(scatter1)
#	print numpy.shape(scatter2)
	scatter_within=scatter1+scatter2
	try:
		v=numpy.dot(linalg.pinv(scatter_within),(mean1-mean2))
	except:
		v=numpy.array(["error in creating v"])
	#find threshold
	if len(v)>1:
		threshold=numpy.dot(v,(mean1+mean2).T)/2.0
	else:
		threshold=0
	# output
	yield(word,str(threshold)+","+json.dumps(v.tolist()))
	#yield(word,str(linalg.det(scatter_within)))

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
