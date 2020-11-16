/#/bin/bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-files mapper.py,reducer.py,combiner.py -mapper mapper.py -combiner combiner.py -reducer reducer.py \
	-input /data/miserables -output wc
