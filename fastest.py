#!/usr/bin/python

import common
import re
import json

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	terms=track_data["tempo"]
	if tempo>0.1:	# if tempo is unknown, it is set as 0
		tempo_string="%07.3f" %tempo
		yield(tempo_string,track_id)

def reduce(word, counts):
	pass

if __name__ == "__main__":
  common.main(map, reduce)
