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
		yield(str(hdf5_getters.get_track_id(h5,0)),json.dumps(output_array))
		h5.close()
		

def reduce(word, counts):
	pass

if __name__ == "__main__":
  common.main(map, reduce)
