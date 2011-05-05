#!/usr/bin/python

# finds tracks with the highest hottness score in each category specified by input file

import common
import json
import re

# input: file name
# output: artist_id artist_name
def map(line):
	if re.match("\d",line):	# if we have a record of which terms to use
		line_split=re.split("\t",line)
		yield(line_split[1],"1")
	else:
		line_split=re.split("\t",line)
		track_id=line_split[0]
		track_data=json.loads(line_split[1])
		hottness=track_data["hottness"]
		if ((hottness>0) and (hottness<1.0)):
			track_name=track_data["title"]
			artist_name=track_data["artist_name"]
			artist_terms=track_data["artist_terms"]
			for term in artist_terms:
				yield(term,str(hottness)+","+artist_name+" -- "+track_name)
				
def reduce(word, counts):
	use_term=0
	artist_array=[]
	for count in counts:
		count_split=re.split(",",count)
		if len(count_split)==1:	# if we have a record of which term to use
			use_term=1;
		else:
			artist_array.append(count_split)
	if use_term==1:
		sorted_array=sorted(artist_array, key=lambda artist_array: artist_array[0])
		for i in range(1,11):
			yield(word,sorted_array[len(sorted_array)-i][1]+" ("+sorted_array[len(sorted_array)-i][0]+")")

if __name__ == "__main__":
  common.main(map, reduce)
