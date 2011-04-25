#!/usr/bin/python

import common
import hdf5_getters

# input: file name
# output: artist_id artist_name
def map(line):
	h5 = hdf5_getters.open_h5_file_read(line)
	if(h5):
		loudness=hdf5_getters.get_segments_loudness_start(h5,0)
		if len(loudness)>0:
			average_loudness=sum(loudness)/len(loudness)
			variance=0
			for value in loudness:
				variance+=(value-average_loudness)**2
			variance=variance/len(loudness)
			track_id=hdf5_getters.get_title(h5,0)
			artist_name=hdf5_getters.get_artist_name(h5,0)
			variance_string="%010.6f" %variance
			#variance_string="%f" %variance
			yield(variance_string,artist_name+" -- "+track_id)
		h5.close()

def reduce(word, counts):
	pass

if __name__ == "__main__":
  common.main(map, reduce)
