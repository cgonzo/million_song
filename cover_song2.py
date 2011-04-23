#!/usr/bin/python

import common
import re

# mapper 
# input
# track ID: cover song ID, artist ID, date
# output
# cover song ID: artist ID, date
def map(line):
	if(line):
		line_split=re.split("\t",line)
		if(len(line_split)==2):
			track_id=line_split[0]
			value_split=re.split(",",line_split[1])
			if(len(value_split)==3):
				coversong_id=value_split[0]
				artist_id=value_split[1]
				date=value_split[2]
				yield(coversong_id,artist_id+","+date)

# reducer outputs
# newer artist ID: oldest artist ID
# 
# next step will combine these into a link map
def reduce(word, counts):
	coversong_id=word
	oldest_date_index=0
	for i in range(len(counts)):
		count_split=re.split(",",count[i])
		if(len(count_split)==2):
			artist_id[i]=count_split[0]
			date[i]=count_split[1]
			if(date[i]<date[oldest_date_index]):
				oldest_date_index=i
	for artist in artist_id:
		if(artist != artist_id[oldest_date_index]):
			yield(artist,artist_id[oldest_date_index])

if __name__ == "__main__":
  common.main(map, reduce)
