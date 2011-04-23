hadoop fs -rmr cover_song1
hadoop jar $SJAR -mapper "/usr/bin/python cover_song1.py map" -reducer "/usr/bin/python cover_song1.py reduce" -input cover_songs.txt -input tracks_per_year.txt -output cover_song1 -file "cover_song1.py" -file "common.py"
hadoop fs -rmr cover_song2
hadoop jar $SJAR -mapper "/usr/bin/python cover_song2.py map" -reducer "/usr/bin/python cover_song2.py reduce" -input cover_song1 -output cover_song2 -file "cover_song2.py" -file "common.py"
hadoop fs -rmr linkmap0
hadoop jar $SJAR -mapper "/usr/bin/python cover_song3.py map" -reducer "/usr/bin/python cover_song3.py reduce" -input cover_song2 -output linkmap0 -file "cover_song3.py" -file "common.py"
for i in {0..9}
do
input_linkmap="linkmap$i"
output_linkmap="linkmap$((i+1))"
reducer_output="results$i"
hadoop fs -rmr $output_linkmap
if [ $2 ]
then
echo "Using $2 reducers"
hadoop jar $SJAR -mapper "/usr/bin/python pagerank.py map" -reducer "/usr/bin/python pagerank.py reduce" -input $input_linkmap -output $output_linkmap -numReduceTasks $2 -file "pagerank.py" -file "common.py"
else
echo "Using default reducers"
hadoop jar $SJAR -mapper "/usr/bin/python pagerank.py map" -reducer "/usr/bin/python pagerank.py reduce" -input $input_linkmap -output $output_linkmap -file "pagerank.py" -file "common.py"
fi
hadoop fs -rmr $reducer_output
hadoop jar $SJAR -mapper "/usr/bin/python pr_out.py map" -reducer "/usr/bin/sort" -input $output_linkmap -output $reducer_output -file "pr_out.py" -file "common.py"
done
