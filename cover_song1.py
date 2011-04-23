#!/usr/bin/python

import common
import re

# mapper outputs 
# if cover song record
# track ID: cover song ID, artist ID
# if track record
# track ID: date
def map(line):
	if(line):
		# we have to see what input line we have
		if (line[0]=="%"): # start of new record
			line_split=re.split("\t",line)
			coversong_match=re.match("%(\d*),",line_split[0])
			if(coversong_match):
				coversong_id=coversong_match.group(0)
				for i in range(1,len(line_split)):
					track_match=re.match("([A-Z0-9]*)<SEP>([A-Z0-9]*)",line_split[i])
					if(track_match):
						track_id=track_match.group(0)
						artist_id=track_match.group(1)
						yield(track_id,coversong_id+","+artist_id)
		else: # track record
			line_split=re.split("<SEP>",line)
			track_date=line_split[0]
			track_id=line_split[1]
			yield(track_id,track_date)

# reducer outputs
# track ID: cover song ID, artist ID, date
def reduce(word, counts):
	# we should have one cover song and one track ID record per song
	if(len(counts)!=2):
		pass
	track_id=word
	for count in counts:
		count_split=re.split(",",count)
		if(count_split[1]):
			# cover song record
			coversong_id=count_split[0]
			artist_id=count_split[1]
		else:
			track_date=count_split[0]
	yield(track_id,cover_song_id+artist_id+track_date)

if __name__ == "__main__":
  common.main(map, reduce)
