hadoop fs -rmr cover_song1
hadoop jar $SJAR -mapper "/usr/bin/python cover_song1.py map" -reducer "/usr/bin/python cover_song1.py reduce" -input cover_songs.txt -input tracks_per_year.txt -output cover_song1 -file "cover_song1.py" -file "common.py"
