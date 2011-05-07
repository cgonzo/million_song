#hadoop fs -rmr build_fisher
#hadoop jar $SJAR -numReduceTasks 10 -mapper "/usr/bin/python build_fisher.py map" -reducer "/usr/bin/python build_fisher.py reduce" -input data -output build_fisher -file "build_fisher.py" -file "common.py" -file "artists_train.txt" -file "most_popular_terms_sorted.txt"
hadoop fs -rmr fisher_classify
hadoop jar $SJAR -mapper "/usr/bin/python fisher_classify.py map" -reducer "/usr/bin/python fisher_classify.py reduce" -input data -output fisher_classify -file "fisher_classify.py" -file "common.py" -file "artists_train.txt" -cacheFile "hdfs://master:54310/user/root/build_fisher/#build_fisher"

