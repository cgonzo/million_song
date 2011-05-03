hadoop fs -rmr artist_by_most_popular_term
hadoop jar $SJAR -mapper "/usr/bin/python artist_by_most_popular_term.py map" -reducer "/usr/bin/python artist_by_most_popular_term.py reduce" -input data -output artist_by_most_popular_term -file "artist_by_most_popular_term.py" -file "common.py"
