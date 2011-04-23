hadoop fs -rmr cover_song1
hadoop jar $SJAR -mapper "/usr/bin/python cover_song1.py map" -reducer "/usr/bin/python cover_song1.py reduce" -input cover_songs.txt -input tracks_per_year.txt -output cover_song1 -file "cover_song1.py" -file "common.py"
hadoop fs -rmr cover_song2
hadoop jar $SJAR -mapper "/usr/bin/python cover_song2.py map" -reducer "/usr/bin/python cover_song2.py reduce" -input cover_song1 -output cover_song2 -file "cover_song2.py" -file "common.py"
