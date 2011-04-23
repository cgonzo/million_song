#!/usr/bin/python

import common
import re

# mapper 
# none
def map(line):
	pass

# reducer
# input
# newer artist ID: oldest artist ID
# output
# artist: artists covered
def reduce(word, counts):
	yield(word,json.dumps(counts)

if __name__ == "__main__":
  common.main(map, reduce)
