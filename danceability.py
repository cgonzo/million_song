#!/usr/bin/python

import common
import json
import re

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	danceability=track_data["danceability"]
	artist_name=track_data["artist_name"]
	yield(artist_name,str(danceability))

def reduce(word, counts):
	average_danceability=0.0
	num_danceable_songs=0
	for count in counts:
		if float(count)>0:
			average_danceability+=float(count)
			num_danceable_songs+=1
	if num_danceable_songs>0:
		average_danceability/=num_danceable_songs
	average_danceability_string="%010.10f"%average_danceability
	yield(average_danceability_string,word)

if __name__ == "__main__":
  common.main(map, reduce)
