hadoop fs -rmr most_popular_terms
hadoop jar $SJAR -mapper "/usr/bin/python most_popular_terms.py map" -reducer "/usr/bin/python most_popular_terms.py reduce" -input data -output most_popular_terms -file "most_popular_terms.py" -file "common.py"
 
hadoop fs -copyToLocal most_popular_terms/part-00000 most_popular_terms.txt
sort most_popular_terms.txt | tail > most_popular_terms_sorted.txt
