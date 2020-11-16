#/bin/bash
hdfs dfs -rmdir wcflic
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-files mapper_flikr.py,reducer_flickr.py,country.py  \
	-mapper mapper_flikr.py -reducer reducer_flickr.py -input flickrSample.txt -output wcflic

