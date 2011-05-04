#!/usr/bin/python

# find song with highest variance in loudness

import common
import hdf5_getters

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	loudness_variance=track_data["segment_loudness_variance"]
	variance_string="%010.6f" %variance
	track_name=track_data["title"]
	artist_name=track_data["artist_name"]
	yield(variance_string,artist_name+" -- "+track_name)

def reduce(word, counts):
	pass

if __name__ == "__main__":
  common.main(map, reduce)
