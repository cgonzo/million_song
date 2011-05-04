hadoop fs -rmr loudness
hadoop jar $SJAR -mapper "/usr/bin/python loudness.py map" -reducer /usr/bin/sort -input data -output loudness -file "loudness.py" -file "common.py"
