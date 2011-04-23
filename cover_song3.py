#!/usr/bin/python

import common
import re
import json

# mapper 
# none
def map(line):
	if(line):
		line_split=re.split("\t",line)
		yield(line_split[0],line_split[1])
# reducer
# input
# newer artist ID: oldest artist ID
# output
# artist: artists covered
def reduce(word, counts):
	pagerank=1.0
	data_to_output=[pagerank, counts]
	yield(word,json.dumps(data_to_output))

if __name__ == "__main__":
  common.main(map, reduce)
