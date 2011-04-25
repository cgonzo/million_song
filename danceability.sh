hadoop fs -rm filelist1.txt
hadoop fs -copyFromLocal filelist1.txt filelist1.txt
hadoop fs -rmr average_tempo
hadoop jar $SJAR -mapper "/usr/bin/python average_tempo.py map" -reducer "/usr/bin/python average_tempo.py reduce" -input filelist1.txt -output average_tempo -file "average_tempo.py" -file "common.py" -file "hdf5_getters.py"
