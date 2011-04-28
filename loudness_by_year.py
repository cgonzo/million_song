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
			year=hdf5_getters.get_year(h5,0)
			yield(str(year),str(variance))
		h5.close()

def reduce(word, counts):
	average=0
	for count in counts:
		average+=float(count)
	average/=len(counts)
	yield(word,str(average))

if __name__ == "__main__":
  common.main(map, reduce)
