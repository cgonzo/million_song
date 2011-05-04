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
	terms=track_data["artist_terms"]
	for term in terms:
		yield(term,"1")

def reduce(word, counts):
	count_sum_string="%010d"%sum([int(count) for count in counts])
	yield(count_sum_string,word)

if __name__ == "__main__":
  common.main(map, reduce)
