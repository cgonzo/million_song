#!/usr/bin/python

import classifiers_base
import common
import hdf5_getters
import json
import sys
import re

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	if(h5):
		output_array=classifiers_base.classify(h5)
		artist_terms=hdf5_getters.get_artist_terms(h5,0)
		f=open('most_popular_terms_sorted.txt')
		for line in f:
			stripped_line=line.rstrip()
			match=0
			for term in artist_terms:
				if (term==stripped_line):
					match=1
			if match==1:
				for i in range(len(output_array)):
					yield(stripped_line+","+str(i),str(output_array[i]))
			else:
				for i in range(len(output_array)):
					yield("!"+stripped_line+","+str(i),str(output_array[i]))
		f.close()
		h5.close()
		

def reduce(word, counts):
	# find out what category and stat we're on
	split_word=re.split(",",word)
	category=split_word[0]
	classifier_number=split_word[1]
	# zero out arrays
	mean=0
	variance=0
	# find mean of all terms
	for count in counts:
		mean+=float(count)
	mean/=len(counts)
	# find variance of all terms
	for count in counts:
		variance+=(float(count)-mean)**2
	variance/=len(counts)
	yield(classifier_number,category+","+str(len(counts))+","+str(mean)+","+str(variance))
	
	

if __name__ == "__main__":
  common.main(map, reduce)
