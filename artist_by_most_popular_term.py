#!/usr/bin/python

import common
import hdf5_getters
import re

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	if(h5):
		terms=hdf5_getters.get_artist_terms(h5,0)
		if len(terms)>0:
			term_frequencies=hdf5_getters.get_artist_terms_freq(h5,0)
			artist_name=hdf5_getters.get_artist_name(h5,0)
			top_term=0
			for i in range(len(terms)):
				if(term_frequencies[i]>term_frequencies[top_term]):
					top_term=i
			yield(terms[top_term],artist_name)
		h5.close()

def reduce(word, counts):
	yield(word,str(len(counts)))

if __name__ == "__main__":
  common.main(map, reduce)
