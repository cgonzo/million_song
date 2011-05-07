hadoop fs -rmr most_generic_pop
hadoop jar $SJAR -mapper "/usr/bin/python most_generic_pop.py map" -reducer /usr/bin/sort -input data -output most_generic_pop -file "most_generic_pop.py" -file "common.py" -file "artists_train.txt" -cacheFile "hdfs://master:54310/user/root/build_fisher/#build_fisher"

