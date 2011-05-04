#!/usr/bin/python

# returns number of songs for each artist

import common
import json
import re

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	tempo=track_data["tempo"]
	artist_id=track_data["artist_id"]
	artist_name=track_data["artist_name"]
	yield(artist_id,artist_name)

def reduce(word, counts):
	count=0
	for artist in counts:
		count=count+1
	yield(counts[0],str(count))

if __name__ == "__main__":
  common.main(map, reduce)
