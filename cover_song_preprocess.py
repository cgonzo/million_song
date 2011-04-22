#!/usr/bin/python

# cover_song_preprocess
# preprocesses the cover song database to turn it into single-line records

import sys

old_line=''
for line in sys.stdin:
	stripped_line=line.rstrip()
	if(stripped_line[0]=='%'):
		print old_line+'\n'
		old_line=stripped_line
	else:
		old_line+='\t'+stripped_line
print old_line+'\n'

	