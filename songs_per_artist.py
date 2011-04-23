#!/usr/bin/python

import common
import hdf5_getters

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	num_songs = hdf5_getters.get_num_songs(h5)
	artist_id=hdf5_getters.get_artist_id(h5,0)
	artist_name=hdf5_getters.get_artist_name(h5,0)
	yield(artist_id,artist_name)

def reduce(word, counts):
	count=0
	for artist in counts:
		count=count+1
	yield(counts[0],str(count))

if __name__ == "__main__":
  common.main(map, reduce)
