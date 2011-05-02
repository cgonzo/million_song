#!/usr/bin/python

import classifiers_base
import common
import hdf5_getters
import json
import sys

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
				yield(stripped_line,json.dumps(output_array))
			else:
				yield("!"+stripped_line,json.dumps(output_array))
		f.close()
		h5.close()
		

def reduce(word, counts):
	# zero out arrays
	mean=[]
	variance=[]
	for iterator in json.loads(counts[0]):
		mean.append(0)
		variance.append(0)
	# find mean of all terms
	for count in counts:
		song_data=json.loads(count)
		for i in range(len(song_data)):
			mean[i]+=song_data[i]
	for i in range(len(mean)):
		mean[i]/=len(counts)
	# find variance of all terms
	for count in counts:
		song_data=json.loads(count)
		for i in range(len(song_data)):
			variance[i]+=(song_data[i]-mean[i])**2
	for i in range(len(mean)):
		variance[i]/=len(counts)
	yield(word,json.dumps([len(counts),mean,variance]))
	
	

if __name__ == "__main__":
  common.main(map, reduce)
