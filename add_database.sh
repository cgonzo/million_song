hadoop fs -rm filelist.txt
hadoop fs -copyFromLocal /mnt/data/filelist.txt filelist.txt
hadoop fs -rmr data
hadoop jar $SJAR -D mapred.map.tasks=80 -mapper "/usr/bin/python add_database.py map" -reducer NONE -input filelist.txt -output data -cmdenv LD_LIBRARY_PATH=$LD_LIBRARY_PATH -file "add_database.py" -file "common.py" -file "classifiers_base.py" -file "hdf5_getters.py"
