#!/usr/bin/python

import common
import json

# input: file name
# output: artist_id artist_name
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	tempo=track_data["tempo"]
	if tempo>0.1:	# if tempo is unknown, set as 0
		yield("1",str(tempo))

def reduce(word, counts):
	tempo_total=0
	for count in counts:
		tempo_total+=float(count)
	tempo_average=tempo_total/len(counts)
	yield("average",str(tempo_average))

if __name__ == "__main__":
  common.main(map, reduce)
