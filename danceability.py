#!/usr/bin/python

import common
import hdf5_getters
import re

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	if(h5):
		danceability=hdf5_getters.get_danceability(h5,0)
		if(danceability>0):
			artist_name=hdf5_getters.get_artist_name(h5,0)
			yield(artist_name,str(danceability))
		h5.close()

def reduce(word, counts):
	average_danceability=0.0
	for count in counts:
		average_danceability+=float(counts)
	average_danceability/=len(counts)
	average_danceability_string="%010.10f"%average_danceability
	yield(average_danceability_string,word)

if __name__ == "__main__":
  common.main(map, reduce)
