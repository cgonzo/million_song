# have to run most_popular_terms first and copy most_popular_terms_sorted.txt to results folder
hadoop fs -rm most_popular_terms_sorted.txt
hadoop fs -copyFromLocal /mnt/data/results/most_popular_terms_sorted.txt most_popular_terms_sorted.txt
# run hottness on them
hadoop fs -rmr hottness
hadoop jar $SJAR -mapper "/usr/bin/python hottness.py map" -reducer "/usr/bin/python hottness.py reduce" -input data -input most_popular_terms_sorted.txt -output hottness -file "hottness.py" -file "common.py"
