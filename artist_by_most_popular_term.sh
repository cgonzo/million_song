hadoop fs -rmr artist_by_most_popular_term
hadoop jar $SJAR -mapper "/usr/bin/python artist_by_most_popular_term.py map" -reducer "/usr/bin/python artist_by_most_popular_term.py reduce" -input data -output artist_by_most_popular_term -file "artist_by_most_popular_term.py" -file "common.py"
hadoop fs -copyToLocal artist_by_most_popular_term/part-00000 artist_by_most_popular_term.txt
sort artist_by_most_popular_term.txt | tail > artist_by_most_popular_term_sorted.txt
hadoop fs -copyFromLocal artist_by_most_popular_term_sorted.txt artist_by_most_popular_term_sorted.txt