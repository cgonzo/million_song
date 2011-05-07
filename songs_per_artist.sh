#export SJAR=/usr/lib/hadoop/contrib/streaming/hadoop-streaming-0.20.2-CDH3B4.jar
hadoop fs -copyFromLocal filelist.txt filelist.txt
hadoop jar $SJAR -mapper "/usr/bin/python songs_per_artist.py map" -reducer "/usr/bin/python songs_per_artist.py reduce" -input data -output songs_per_artist -file "songs_per_artist.py" -file "common.py" -file "hdf5_getters.py"

