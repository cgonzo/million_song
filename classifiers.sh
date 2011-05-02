hadoop fs -rm filelist.txt
hadoop fs -copyFromLocal filelist.txt filelist.txt
hadoop fs -rmr classifiers
hadoop jar $SJAR -mapper "/usr/bin/python classifiers.py map" -reducer "/usr/bin/python classifiers.py reduce" -input filelist.txt -output classifiers -file "classifiers.py" -file "common.py" -file "hdf5_getters.py" -file "most_popular_terms_sorted.txt"
