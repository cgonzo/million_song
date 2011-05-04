hadoop fs -rmr loudness_by_year
hadoop jar $SJAR -mapper "/usr/bin/python loudness_by_year.py map" -reducer "/usr/bin/python loudness_by_year.py reduce" -input data -output loudness_by_year -file "loudness_by_year.py" -file "common.py"
