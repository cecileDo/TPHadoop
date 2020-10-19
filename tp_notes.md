# TP hadooop

### 3.1 HDFS
boukamec@im2ag-hadoop-01:~$ hdfs dfs \\
Usage: hadoop fs [generic options] \\
	[-appendToFile <localsrc> ... <dst>] \\
	[-cat [-ignoreCrc] <src> ...] \\
	[-checksum <src> ...]
	[-chgrp [-R] GROUP PATH...]
	[-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
	[-chown [-R] [OWNER][:[GROUP]] PATH...]
	[-copyFromLocal [-f] [-p] [-l] [-d] [-t <thread count>] <localsrc> ... <dst>]
	[-copyToLocal [-f] [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
	[-count [-q] [-h] [-v] [-t [<storage type>]] [-u] [-x] [-e] <path> ...]
	[-cp [-f] [-p | -p[topax]] [-d] <src> ... <dst>]
	[-createSnapshot <snapshotDir> [<snapshotName>]]
	[-deleteSnapshot <snapshotDir> <snapshotName>]
	[-df [-h] [<path> ...]]
	[-du [-s] [-h] [-v] [-x] <path> ...]
	[-expunge]
	[-find <path> ... <expression> ...]
	[-get [-f] [-p] [-ignoreCrc] [-crc] <src> ... <localdst>]
	[-getfacl [-R] <path>]
	[-getfattr [-R] {-n name | -d} [-e en] <path>]
	[-getmerge [-nl] [-skip-empty-file] <src> <localdst>]
	[-head <file>]
	[-help [cmd ...]]
	[-ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [-e] [<path> ...]]
	[-mkdir [-p] <path> ...]
	[-moveFromLocal <localsrc> ... <dst>]
	[-moveToLocal <src> <localdst>]
	[-mv <src> ... <dst>]
	[-put [-f] [-p] [-l] [-d] <localsrc> ... <dst>]
	[-renameSnapshot <snapshotDir> <oldName> <newName>]
	[-rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ...]
	[-rmdir [--ignore-fail-on-non-empty] <dir> ...]
	[-setfacl [-R] [{-b|-k} {-m|-x <acl_spec>} <path>]|[--set <acl_spec> <path>]]
	[-setfattr {-n name [-v value] | -x name} <path>]
	[-setrep [-R] [-w] <rep> <path> ...]
	[-stat [format] <path> ...]
	[-tail [-f] <file>]
	[-test -[defsz] <path>]
	[-text [-ignoreCrc] <src> ...]
	[-touch [-a] [-m] [-t TIMESTAMP ] [-c] <path> ...]
	[-touchz <path> ...]
	[-truncate [-w] <length> <path> ...]
	[-usage [cmd ...]]
$

Generic options supported are:
-conf <configuration file>        specify an application configuration file
-D <property=value>               define a value for a given property
-fs <file:///|hdfs://namenode:port> specify default filesystem URL to use, overrides 'fs.defaultFS' property from configurations.
-jt <local|resourcemanager:port>  specify a ResourceManager
-files <file1,...>                specify a comma-separated list of files to be copied to the map reduce cluster
-libjars <jar1,...>               specify a comma-separated list of jar files to be included in the classpath
-archives <archive1,...>          specify a comma-separated list of archives to be unarchived on the compute machines

The general command line syntax is:
command [genericOptions] [commandOptions]
boukamec@im2ag-hadoop-01:~$ hdfs dfs -ls /
Found 3 items
drwxr-xr-x   - hduser hdgroup          0 2020-03-30 10:52 /data
drwxrwxrwt   - hduser hdgroup          0 2020-04-08 11:15 /tmp
drwxr-xr-x   - hduser hdgroup          0 2020-10-09 16:12 /user
$
\end{multline}
boukamec@im2ag-hadoop-01:~/tp_mapReduce$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar 
-files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /data/Miserables -output wc
$
packageJobJar: [/tmp/hadoop-unjar1278807324047468681/] [] /tmp/streamjob530482950002622574.jar tmpDir=null
2020-10-11 15:56:10,615 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-10-11 15:56:10,803 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-10-11 15:56:11,063 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/boukamec/.staging/job_1602376086513_0003
2020-10-11 15:56:11,473 INFO mapred.FileInputFormat: Total input files to process : 3
2020-10-11 15:56:11,599 INFO mapreduce.JobSubmitter: number of splits:3
2020-10-11 15:56:11,810 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1602376086513_0003
2020-10-11 15:56:11,812 INFO mapreduce.JobSubmitter: Executing with tokens: []
2020-10-11 15:56:11,997 INFO conf.Configuration: resource-types.xml not found
2020-10-11 15:56:11,998 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2020-10-11 15:56:12,059 INFO impl.YarnClientImpl: Submitted application application_1602376086513_0003
2020-10-11 15:56:12,120 INFO mapreduce.Job: The url to track the job: http://im2ag-hadoop-01.u-ga.fr:8088/proxy/application_1602376086513_0003/
2020-10-11 15:56:12,122 INFO mapreduce.Job: Running job: job_1602376086513_0003
2020-10-11 15:56:18,274 INFO mapreduce.Job: Job job_1602376086513_0003 running in uber mode : false
2020-10-11 15:56:18,275 INFO mapreduce.Job:  map 0% reduce 0%
2020-10-11 15:56:25,360 INFO mapreduce.Job:  map 67% reduce 0%
2020-10-11 15:56:26,364 INFO mapreduce.Job:  map 100% reduce 0%
2020-10-11 15:56:34,404 INFO mapreduce.Job:  map 100% reduce 100%
2020-10-11 15:56:35,415 INFO mapreduce.Job: Job job_1602376086513_0003 completed successfully
2020-10-11 15:56:35,547 INFO mapreduce.Job: Counters: 55
	File System Counters
		FILE: Number of bytes read=17741099
		FILE: Number of bytes written=36360311
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=9363281
		HDFS: Number of bytes written=2248328
		HDFS: Number of read operations=14
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
	Job Counters
		Killed map tasks=1
		Launched map tasks=3
		Launched reduce tasks=1
		Data-local map tasks=2
		Rack-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=14642
		Total time spent by all reduces in occupied slots (ms)=7028
		Total time spent by all map tasks (ms)=14642
		Total time spent by all reduce tasks (ms)=7028
		Total vcore-milliseconds taken by all map tasks=14642
		Total vcore-milliseconds taken by all reduce tasks=7028
		Total megabyte-milliseconds taken by all map tasks=29284000
		Total megabyte-milliseconds taken by all reduce tasks=14056000
	Map-Reduce Framework
		Map input records=180595
		Map output records=1439046
		Map output bytes=14860430
		Map output materialized bytes=17741111
		Input split bytes=351
		Combine input records=0
		Combine output records=0
		Reduce input groups=127343
		Reduce shuffle bytes=17741111
		Reduce input records=1439046
		Reduce output records=110203
		Spilled Records=2878092
		Shuffled Maps =3
		Failed Shuffles=0
		Merged Map outputs=3
		GC time elapsed (ms)=371
		CPU time spent (ms)=10110
		Physical memory (bytes) snapshot=1263222784
		Virtual memory (bytes) snapshot=10519543808
		Total committed heap usage (bytes)=1519910912
		Peak Map Physical memory (bytes)=352182272
		Peak Map Virtual memory (bytes)=2629148672
		Peak Reduce Physical memory (bytes)=252039168
		Peak Reduce Virtual memory (bytes)=2634395648
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters
		Bytes Read=9362930
	File Output Format Counters
		Bytes Written=2248328
2020-10-11 15:56:35,548 INFO streaming.StreamJob: Output directory: wc


boukamec@im2ag-hadoop-01:~/tp_mapReducehdfs dfs -ls
Found 1 items
drwxr-xr-x   - boukamec boukamec          0 2020-10-11 15:56 wc
boukamec@im2ag-hadoop-01:~/tp_mapReduce$ hdfs dfs -ls wc
Found 2 items
-rw-r--r--   1 boukamec boukamec          0 2020-10-11 15:56 wc/_SUCCESS
-rw-r--r--   1 boukamec boukamec    2248328 2020-10-11 15:56 wc/part-00000
***Question Regardez attentivement le déroulement de l’exécution ainsi que l’affichage du comportement de Hadoop. Retrouvez le nombre de “splits” lus sur HDFS. A quel compteur ce nombre
correspond-il ?***
le nombre de packets de 64MB nécessaires a stocker les données
2020-10-11 15:56:11,599 INFO mapreduce.JobSubmitter: number of splits:3

Où sont les résultats du job Hadoop ?
dans le ~/wc (repertoire donné en paramètre du --output)

### 3.3 Ajout d’un combiner

***Question À partir du cours, déduisez ce que doit faire le combiner pour le programme wordcount.
Déduisez-en le code du programme Python combiner.py
combiner.py doit prendre en entrée des liste key avec liste de valeur et les sommer***

c'est le même code que le reducer mais en sommant les valeurs à l'interieur d'un clister

oukamec@im2ag-hadoop-01:~/tp_mapReduce$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar -files mapper.py,reducer.py,combiner.py -mapper ma
pper.py -combiner combiner.py -reducer reducer.py -input /data/miserables -output wc
packageJobJar: [/tmp/hadoop-unjar6348337114372431690/] [] /tmp/streamjob5450684265884880911.jar tmpDir=null
2020-10-11 17:29:38,754 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-10-11 17:29:38,941 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-10-11 17:29:39,198 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/boukamec/.staging/job_1602376086513_0004
2020-10-11 17:29:39,696 INFO mapred.FileInputFormat: Total input files to process : 5
2020-10-11 17:29:39,832 INFO mapreduce.JobSubmitter: number of splits:5
2020-10-11 17:29:39,998 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1602376086513_0004
2020-10-11 17:29:40,000 INFO mapreduce.JobSubmitter: Executing with tokens: []
2020-10-11 17:29:40,170 INFO conf.Configuration: resource-types.xml not found
2020-10-11 17:29:40,170 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2020-10-11 17:29:40,431 INFO impl.YarnClientImpl: Submitted application application_1602376086513_0004
2020-10-11 17:29:40,470 INFO mapreduce.Job: The url to track the job: http://im2ag-hadoop-01.u-ga.fr:8088/proxy/application_1602376086513_0004/
2020-10-11 17:29:40,471 INFO mapreduce.Job: Running job: job_1602376086513_0004
2020-10-11 17:29:46,615 INFO mapreduce.Job: Job job_1602376086513_0004 running in uber mode : false
2020-10-11 17:29:46,616 INFO mapreduce.Job:  map 0% reduce 0%
2020-10-11 17:29:54,716 INFO mapreduce.Job:  map 60% reduce 0%
2020-10-11 17:29:56,728 INFO mapreduce.Job:  map 100% reduce 0%
2020-10-11 17:30:00,746 INFO mapreduce.Job:  map 100% reduce 100%
2020-10-11 17:30:00,755 INFO mapreduce.Job: Job job_1602376086513_0004 completed successfully
2020-10-11 17:30:00,848 INFO mapreduce.Job: Counters: 55
	File System Counters
		FILE: Number of bytes read=1223114
		FILE: Number of bytes written=3767337
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2536158
		HDFS: Number of bytes written=676452
		HDFS: Number of read operations=20
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
	Job Counters
		Killed map tasks=1
		Launched map tasks=5
		Launched reduce tasks=1
		Data-local map tasks=4
		Rack-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=31282
		Total time spent by all reduces in occupied slots (ms)=3706
		Total time spent by all map tasks (ms)=31282
		Total time spent by all reduce tasks (ms)=3706
		Total vcore-milliseconds taken by all map tasks=31282
		Total vcore-milliseconds taken by all reduce tasks=3706
		Total megabyte-milliseconds taken by all map tasks=62564000
		Total megabyte-milliseconds taken by all reduce tasks=7412000
	Map-Reduce Framework
		Map input records=52711
		Map output records=421826
		Map output bytes=4167915
		Map output materialized bytes=1223138
		Input split bytes=620
		Combine input records=421826
		Combine output records=85296
		Reduce input groups=85296
		Reduce shuffle bytes=1223138
		Reduce input records=85296
		Reduce output records=52554
		Spilled Records=170592
		Shuffled Maps =5
		Failed Shuffles=0
		Merged Map outputs=5
		GC time elapsed (ms)=695
		CPU time spent (ms)=10660
		Physical memory (bytes) snapshot=1992359936
		Virtual memory (bytes) snapshot=15782191104
		Total committed heap usage (bytes)=2069889024
		Peak Map Physical memory (bytes)=359219200
		Peak Map Virtual memory (bytes)=2634059776
		Peak Reduce Physical memory (bytes)=250576896
		Peak Reduce Virtual memory (bytes)=2628329472
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters
		Bytes Read=2535538
	File Output Format Counters
		Bytes Written=676452
2020-10-11 17:30:00,849 INFO streaming.StreamJob: Output directory: wc

## 3.4 Plusieurs reducers

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -numReduceTasks 3 -input /data/miserables -output wc

packageJobJar: [/tmp/hadoop-unjar3312545640244393523/] [] /tmp/streamjob9071507183851081788.jar tmpDir=null
2020-10-12 15:08:48,697 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-10-12 15:08:48,921 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-10-12 15:08:49,209 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/boukamec/.staging/job_1602462488126_0001
2020-10-12 15:08:50,833 INFO mapred.FileInputFormat: Total input files to process : 5
2020-10-12 15:08:51,728 INFO mapreduce.JobSubmitter: number of splits:5
2020-10-12 15:08:52,245 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1602462488126_0001
2020-10-12 15:08:52,247 INFO mapreduce.JobSubmitter: Executing with tokens: []
2020-10-12 15:08:52,435 INFO conf.Configuration: resource-types.xml not found
2020-10-12 15:08:52,436 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2020-10-12 15:08:52,934 INFO impl.YarnClientImpl: Submitted application application_1602462488126_0001
2020-10-12 15:08:52,985 INFO mapreduce.Job: The url to track the job: http://im2ag-hadoop-01.u-ga.fr:8088/proxy/application_1602462488126_0001/
2020-10-12 15:08:52,988 INFO mapreduce.Job: Running job: job_1602462488126_0001
2020-10-12 15:09:03,338 INFO mapreduce.Job: Job job_1602462488126_0001 running in uber mode : false
2020-10-12 15:09:03,339 INFO mapreduce.Job:  map 0% reduce 0%
2020-10-12 15:09:10,470 INFO mapreduce.Job:  map 20% reduce 0%
2020-10-12 15:09:14,517 INFO mapreduce.Job:  map 60% reduce 0%
2020-10-12 15:09:17,537 INFO mapreduce.Job:  map 100% reduce 0%
2020-10-12 15:09:19,549 INFO mapreduce.Job:  map 100% reduce 100%
2020-10-12 15:09:20,564 INFO mapreduce.Job: Job job_1602462488126_0001 completed successfully
2020-10-12 15:09:20,681 INFO mapreduce.Job: Counters: 55
	File System Counters
		FILE: Number of bytes read=5011585
		FILE: Number of bytes written=11779621
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2536158
		HDFS: Number of bytes written=739375
		HDFS: Number of read operations=30
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=6
	Job Counters 
		Killed map tasks=1
		Launched map tasks=5
		Launched reduce tasks=3
		Data-local map tasks=4
		Rack-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=41795
		Total time spent by all reduces in occupied slots (ms)=17559
		Total time spent by all map tasks (ms)=41795
		Total time spent by all reduce tasks (ms)=17559
		Total vcore-milliseconds taken by all map tasks=41795
		Total vcore-milliseconds taken by all reduce tasks=17559
		Total megabyte-milliseconds taken by all map tasks=83590000
		Total megabyte-milliseconds taken by all reduce tasks=35118000
	Map-Reduce Framework
		Map input records=52711
		Map output records=421826
		Map output bytes=4167915
		Map output materialized bytes=5011657
		Input split bytes=620
		Combine input records=0
		Combine output records=0
		Reduce input groups=60473
		Reduce shuffle bytes=5011657
		Reduce input records=421826
		Reduce output records=57972
		Spilled Records=843652
		Shuffled Maps =15
		Failed Shuffles=0
		Merged Map outputs=15
		GC time elapsed (ms)=996
		CPU time spent (ms)=16460
		Physical memory (bytes) snapshot=2516959232
		Virtual memory (bytes) snapshot=21058289664
		Total committed heap usage (bytes)=2581069824
		Peak Map Physical memory (bytes)=363466752
		Peak Map Virtual memory (bytes)=2640850944
		Peak Reduce Physical memory (bytes)=251191296
		Peak Reduce Virtual memory (bytes)=2633662464
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=2535538
	File Output Format Counters 
		Bytes Written=739375
2020-10-12 15:09:20,682 INFO streaming.StreamJob: Output directory: wc


** Question Comment se présente le résultat ? Pourquoi ? ***
sous forme de 3 fichiers part-00000 part-00001 part-00002
ce sont les sorties des Reducers 

# 4 Top-tags Flickr par pays

*** Dans la suite de ce TP vous allez étudier des méta-données de photos stockées dans un jeu de
données de Flickr. À chaque photo est associé par l’utilisateur un ensemble de tags ainsi que les
coordonnées GPS où la photo a été prise. Le but sera de trouver à partir de ces données pour
chaque pays quels sont les tags les plus fréquents.
Dans l’archive que vous avez téléchargée se trouvent trois fichiers :
• flickrSpecs.txt contient le format du fichier de données.
• flickrSample.txt contient un extrait du fichier de données que vous pouvez utiliser pour vos
test locaux.
• country.py qui contient le code de la fonction getCountryAt qui prend en paramètres une
latitude et une longitude et renvoie le code du pays de cette coordonnée. N’oubliez pas
d’appeler la fonction init_pays avant de l’appeler la première fois. ***


\end{document}