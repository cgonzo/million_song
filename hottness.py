#!/usr/bin/python

import common
import hdf5_getters
import re

# input: file name
# output: artist_id artist_name
def map(line):
	if re.match("\d",line):	# if we have a record of which terms to use
		line_split=re.split("\t",line)
		yield(line_split[1],"1")
	else:
		h5 = hdf5_getters.open_h5_file_read(line)
		if(h5):
			hottness=hdf5_getters.get_song_hotttnesss(h5,0)
			if(hottness>0):
				track_name=hdf5_getters.get_title(h5,0)
				artist_name=hdf5_getters.get_artist_name(h5,0)
				artist_terms=hdf5_getters.get_artist_terms(h5,0)
				for term in artist_terms:
					yield(term,str(hottness)+","+artist_name+" -- "+track_name)
			h5.close()

def reduce(word, counts):
	use_term=0
	artist_array=[]
	for count in counts:
		count_split=re.split(",",count)
		if len(count_split)==1:	# if we have a record of which term to use
			use_term=1;
		else:
			artist_array.append(count_split)
	if use_term==1:
		sorted_array=sorted(artist_array, key=lambda artist_array: artist_array[0])
		for i in range(1,11):
			yield(word,sorted_array[len(sorted_array)-i][1]+" ("+sorted_array[len(sorted_array)-i][0]+")")

if __name__ == "__main__":
  common.main(map, reduce)
