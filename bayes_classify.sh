hadoop fs -rmr bayes_classify
# no reducer for debugging
#hadoop jar $SJAR -mapper "/usr/bin/python bayes_classify.py map" -reducer NONE -input data -output bayes_classify -file "bayes_classify.py" -file "common.py" -file "artists_train.txt" -cacheFile "hdfs://master:54310/user/root/build_bayes/#build_bayes"
# this one includes reducer
hadoop jar $SJAR -mapper "/usr/bin/python bayes_classify.py map" -reducer "/usr/bin/python bayes_classify.py reduce" -input data -output bayes_classify -file "bayes_classify.py" -file "common.py" -file "artists_train.txt" -cacheFile "hdfs://master:54310/user/root/build_bayes/#build_bayes"
