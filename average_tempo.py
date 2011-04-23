#!/usr/bin/python

import common
import hdf5_getters

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	tempo=hdf5_getters.get_tempo(h5,0)
	yield("1",tempo)

def reduce(word, counts):
	tempo_total=0
	for count in counts:
		tempo_total+=count
	tempo_total/=len(counts)
	

if __name__ == "__main__":
  common.main(map, reduce)
