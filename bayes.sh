hadoop fs -rmr build_bayes
hadoop jar $SJAR -mapper "/usr/bin/python build_bayes.py map" -reducer "/usr/bin/python build_bayes.py reduce" -input data -output build_bayes -file "build_bayes.py" -file "common.py" -file "artists_train.txt"
