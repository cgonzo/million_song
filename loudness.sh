hadoop fs -rm filelist.txt
hadoop fs -copyFromLocal filelist.txt filelist.txt
hadoop fs -rmr loudness
hadoop jar $SJAR -mapper "/usr/bin/python loudness.py map" -reducer /usr/bin/sort -input filelist.txt -output loudness -file "loudness.py" -file "common.py" -file "hdf5_getters.py"
