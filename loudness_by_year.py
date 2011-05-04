#!/usr/bin/python

# gets average of loudness variance per year

import common
import json
import re

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	loudness_variance=track_data["segment_loudness_variance"]
	year=track_data["year"]
	yield(str(year),str(loudness_variance))

def reduce(word, counts):
	average=0
	for count in counts:
		average+=float(count)
	average/=len(counts)
	yield(word,str(average))

if __name__ == "__main__":
  common.main(map, reduce)
