#!/usr/bin/python

import common
import re
import json

# input: page [pagerank [list of links]]
# output: pagerank page 
def map(line):
	# split into key,value
	line_split=re.split('\t',line,maxsplit=1)
	if line_split:	# this should always be true
		linker_name=line_split[0]
		link_data=json.loads(line_split[1])
		pagerank=link_data[0]
  		yield(str(pagerank),linker_name)

def reduce(word, counts):
	yield(word,counts)

if __name__ == "__main__":
  common.main(map, reduce)
