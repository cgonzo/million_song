hadoop fs -rm filelist.txt
hadoop fs -copyFromLocal filelist.txt filelist.txt
hadoop fs -rmr loudness_by_year
hadoop jar $SJAR -mapper "/usr/bin/python loudness_by_year.py map" -reducer "/usr/bin/python loudness_by_year.py reduce" -input filelist.txt -output loudness_by_year -file "loudness_by_year.py" -file "common.py" -file "hdf5_getters.py"
