hadoop fs -rmr average_tempo
hadoop jar $SJAR -mapper "/usr/bin/python average_tempo.py map" -reducer "/usr/bin/python average_tempo.py reduce" -input data -output average_tempo -file "average_tempo.py" -file "common.py"
