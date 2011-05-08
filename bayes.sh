if [ ! -f artist_by_most_popular_term_sorted.txt ]; then
    ./artist_by_most_popular_term.sh
fi
cp /mnt/data/AdditionalFiles/artists_train.txt .
hadoop fs -rmr build_bayes
hadoop jar $SJAR -numReduceTasks 20 -mapper "/usr/bin/python build_bayes.py map" -reducer "/usr/bin/python build_bayes.py reduce" -input data -output build_bayes -file "build_bayes.py" -file "common.py" -file "artists_train.txt" -file "artist_by_most_popular_term_sorted.txt"
hadoop fs -rmr bayes_classify
hadoop jar $SJAR -mapper "/usr/bin/python bayes_classify.py map" -reducer "/usr/bin/python bayes_classify.py reduce" -input data -output bayes_classify -file "bayes_classify.py" -file "common.py" -file "artists_train.txt" -cacheFile "hdfs://master:54310/user/root/build_bayes/#build_bayes"

