#!/usr/bin/python

import common
import hdf5_getters
import re

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	if(h5):
		artist_terms=hdf5_getters.get_artist_terms(h5,0)
		for term in artist_terms:
			yield(term,"1")
		h5.close()

def reduce(word, counts):
	count_sum_string="%010d"%sum([int(count) for count in counts])
	yield(count_sum_string,word)

if __name__ == "__main__":
  common.main(map, reduce)
