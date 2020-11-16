#/bin/bash
hdfs dfs -rmdir wcflic
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar  \
	-files mapper_flikr.py,country.py,reducer_flickr_with_combiner.py,combiner_flickr.py  \
	-mapper mapper_flikr.py -combiner combiner_flickr.py -reducer reducer_flickr_with_combiner.py \
	-input flickrSample.txt -output wcflic

