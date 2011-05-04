hadoop fs -rmr danceability
hadoop jar $SJAR -mapper "/usr/bin/python danceability.py map" -reducer "/usr/bin/python danceability.py reduce" -input data -output danceability -file "danceability.py" -file "common.py"
