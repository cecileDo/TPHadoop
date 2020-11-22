# MS BigData - Stockage et traitement de données à grande échelle

## TP hadoop

Cécile Boukamel-Donnou
__________________

Vous trouverez ci-dessous mes réponses Au TP Haddop ainsi que le code et les résultats obtenus.

Ce document est aussi,pour moi, une aide mémoire.
les sources ainsi que les commandes sont accessibles sur  <https://github.com/cecileDo/TPHadoop>

## 2 Premier contact : wordcount

>Pour démarrer vous allez écrire un programme permettant de compter les mots d’un fichier, comme nous l’avons vu en cours. Vous écrirez deux programmes Python, un pour la phase Map et un autre pour la phase Reduce.  
Écrivez et testez les d’abord en local sur votre machine avant de les exécuter
sur le cluster Hadoop.  
Pour cela vous n’avez pas besoin d’installer autre chose que Python. Vousdevez vous assurer que la sortie du mapper est une suite de lignes contenant un couple (clé, valeur),le séparateur entre les deux étant le caractère de tabulation.

### 2.1 Écriture du mapper

>Dans cette partie vous devez écrire un programme Python mapper.py qui prend en entrée un fichier texte et affiche en sortie chaque mot du fichier avec la valeur 1.

#### mapper.py

```python3

import os
import sys

def mapper_file(afile):
    assert(os.path.isfile(afile)), "CSV file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return mapper(f)

def mapper(lines):
    lst=""
    for line in lines:
        line = line.strip().split(" ")
        lst= lst+mapper_line(line)
    return lst.strip()

def mapper_line(line):
    return  ('\t1\n'.join(line)+'\t1\n')

if __name__ == "__main__":
    #print (mapper_file("data.txt") )
    print (mapper(sys.stdin) )

```

### 2.2 Écriture du reducer

>Vous devez maintenant écrire le reducer, le programme Python reducer.py qui va prendre en entrée la sortie du mapper et afficher en sortie chaque mot avec son nombre d’occurences.  
Pour le fichier exemple précédent il affichera :  
a 2  
b 1  
c 1

#### new mapper.py

```python3
#!/usr/bin/env python

import os
import sys

def mapper_file(afile):
    assert(os.path.isfile(afile)), "CSV file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return mapper(f)

def mapper(lines):
    lst=""
    for line in lines:
        line = line.strip().split(" ")
        lst= lst+mapper_line(line)
    return lst.strip()

def mapper_line(line):
    return  ('\t1\n'.join(line)+'\t1\n')

if __name__ == "__main__":
    #print (mapper_file("data.txt") )
    print (mapper(sys.stdin) )

```

### 3.1 HDFS

```bash

boukamec@im2ag-hadoop-01:~$ hdfs dfs
Usage: hadoop fs [generic options]
     [-appendToFile <localsrc> ... <dst>]
     [-cat [-ignoreCrc] <src> ...]
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
```

>Question Regardez attentivement le déroulement de l’exécution ainsi que l’affichage du comportement de Hadoop. Retrouvez le nombre de “splits” lus sur HDFS.  
A quel compteur ce nombre correspond-il ?

Celui ci correspond au nombre de packets de 64MB nécessaires à stocker les données.  

```bash
2020-10-11 15:56:11,599 INFO mapreduce.JobSubmitter: number of splits:3
```

>Où sont les résultats du job Hadoop ?

dans le repertoire ~/wc (repertoire donné en paramètre --output)

### 3.3 Ajout d’un combiner

>Question À partir du cours, déduisez ce que doit faire le combiner pour le programme wordcount.  
Déduisez-en le code du programme Python combiner.py

combiner.py doit prendre en entrée des liste key avec liste de valeur et les sommer

c'est le même code que le reducer mais en sommant les valeurs à l'interieur d'un cluster

```bash

boukamec@im2ag-hadoop-01:~/tp_mapReduce$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar -files mapper.py,reducer.py,combiner.py -mapper ma
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
```

>Question Le résultat est il le même que sans combiner ?

Oui le résultat est le même

>Sur quels compteurs voyez-vous l’effet du combiner ?

Je ne comprend pas la question

## 3.4 Plusieurs reducers

>Dans toutes les exécutions menées jusqu’à présent, le reduce n’était exécuté que sur un nœud. Nous allons changer cela en exécutant le programme avec la commande suivante :  
regardez la documentation disponible en cas de besoin.  
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar
-files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py
-numReduceTasks 3 -input /data/miserables -output wc

```bash
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
```

>Question Comment se présente le résultat ? Pourquoi ?

Le résultat se présente sous forme de 3 fichiers part-00000 part-00001 part-00002
ce sont les sorties de chaque Reducer.

## 4 Top-tags Flickr par pays

>Dans la suite de ce TP vous allez étudier des méta-données de photos stockées dans un jeu de données de Flickr. À chaque photo est associé par l’utilisateur un ensemble de tags ainsi que les
coordonnées GPS où la photo a été prise. Le but sera de trouver à partir de ces données pour chaque pays quels sont les tags les plus fréquents.
Dans l’archive que vous avez téléchargée se trouvent trois fichiers :
>
> * flickrSpecs.txt contient le format du fichier de données.
> * flickrSample.txt contient un extrait du fichier de données que vous pouvez utiliser pour vos test locaux.
>* country.py qui contient le code de la fonction getCountryAt qui prend en paramètres une latitude et une longitude et renvoie le code du pays de cette coordonnée. N’oubliez pas
d’appeler la fonction init_pays avant de l’appeler la première fois.

### 4.1 Map et Reduce

>On veut trouver les K tags les plus utilisés par pays, une bonne clé intermédiaire entre le mapper et
le reducer semble donc être le code du pays sur 2 caractères retourné par la fonction getCountryAt
fournie.
Dans le reducer il faudra utiliser une structure de données stockant l’ensemble des tags et leur
nombre d’occurence pour ensuite en extraire les plus fréquents.
Écrivez le programme map/reduce réalisant ce traitement. Testez-le localement puis sur le cluster

### mapper_flikr.py

```python3
#!/usr/bin/env python

import os
import sys
import country

longitude_field = 10
latitude_field = 11
tags_field = 8

def mapper_file(afile):
    assert(os.path.isfile(afile)), "CSV file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return mapper(f)

def mapper(lines):
    country.init_pays()
    lst=""
    for line in lines:
        line = line.strip().split("\t")
        #print( line)
        lst= lst+mapper_line(line)
    return lst.strip()

def mapper_line(line):
    res =""
    contry_id = country.getCountryAt(float(line[latitude_field]), float(line[longitude_field]))
    if contry_id == "":
        #print ("No country for ",float(line[latitude_field]), float(line[longitude_field]))
        return ""
    for tag in line[tags_field].split(","):
        #print("Tag : " , tag)
        res+= contry_id+ "\t"+ tag + "\n"
    return  res

if __name__ == "__main__":
    #print (mapper_file("flickrSample.txt") )
    print (mapper(sys.stdin) )

```

#### reducer.py

```python3

#!/usr/bin/env python

import os
import sys
import json
k=4
def reducer_file(afile):
    assert(os.path.isfile(afile)), "file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return reducer(f)


def get_list_best_tag_by_country (data_dict):
    """
    take a list of tag by contry return only k best tags by contry
    """
    res_dict = dict()
    for  country, tags in data_dict.items():
        # get all tag for contry
        lst_tag = list(dict.fromkeys(tags))
        nb_val_tag = [None] * len(lst_tag)
        for i in range(len(lst_tag)):
            nb_val_tag[i]=tags.count(lst_tag[i])
        sorted_lst_tag = [x for _,x in sorted(zip(nb_val_tag,lst_tag), reverse=True)]
        #take k first one
        res_dict[country] = ' '.join(sorted_lst_tag[:4])
    return res_dict

def get_list_tag_by_country(data):
    """
    for each contry build list of tag
    """
    data_dict = dict()
    for line in data:
        if line.strip():
            line = line.strip().split('\t')
            # line contain country tag values
            if len(line) == 2:
                # create a dict of list of tag
                country = line[0]
                if country in data_dict:
                    data_dict[country].append(line[1])
                else:
                    data_dict[country] = [line[1]]
    return data_dict

def reducer(data):
    data_dict = get_list_tag_by_country(data)
    res_dict = get_list_best_tag_by_country(data_dict)
    return '\n'.join(["\t".join([key, str(val)]) for key, val in res_dict.items()])


if __name__ == "__main__":
    print(reducer(sys.stdin) )
    #print(reducer_file("out_mapper_flickr.txt"))

```

Résultat sur un exemple:

```bash
./mapper_flikr.py < /data/flicksample | sort | ./reducer_flickr.py

boukamec@im2ag-hadoop-01:~/tp_hadoop$ ./mapper_flikr.py < flickrSample.txt | sort | ./reducer_flickr.py
ML     mali niger viajes rio+niger
BN     ghana lab idds africa
UV     africa burkina-faso burkina+faso afrique
AG     hoggar amazigh+culture algeria alger
```

Résultat sur le framework: une erreur que je ne parvient pas a corriger

```bash

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar -files mapper_flikr.py,reducer_flickr.py  \
-mapper mapper_flikr.py -reducer reducer_flickr.py -input /data/flicksample -output wcflic

packageJobJar: [/tmp/hadoop-unjar1286712561916788346/] [] /tmp/streamjob3682171857042016209.jar tmpDir=null
2020-11-16 16:01:04,045 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-11-16 16:01:04,226 INFO client.RMProxy: Connecting to ResourceManager at /152.77.81.30:8032
2020-11-16 16:01:04,488 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/boukamec/.staging/job_1605490088936_0045
2020-11-16 16:01:05,241 INFO mapred.FileInputFormat: Total input files to process : 1
2020-11-16 16:01:05,327 WARN hdfs.DataStreamer: Caught exception
java.lang.InterruptedException
     at java.lang.Object.wait(Native Method)
     at java.lang.Thread.join(Thread.java:1252)
     at java.lang.Thread.join(Thread.java:1326)
     at org.apache.hadoop.hdfs.DataStreamer.closeResponder(DataStreamer.java:986)
     at org.apache.hadoop.hdfs.DataStreamer.endBlock(DataStreamer.java:640)
     at org.apache.hadoop.hdfs.DataStreamer.run(DataStreamer.java:810)
2020-11-16 16:01:05,378 INFO mapreduce.JobSubmitter: number of splits:2
2020-11-16 16:01:05,550 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1605490088936_0045
2020-11-16 16:01:05,551 INFO mapreduce.JobSubmitter: Executing with tokens: []
2020-11-16 16:01:05,750 INFO conf.Configuration: resource-types.xml not found
2020-11-16 16:01:05,751 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2020-11-16 16:01:05,810 INFO impl.YarnClientImpl: Submitted application application_1605490088936_0045
2020-11-16 16:01:05,844 INFO mapreduce.Job: The url to track the job: http://im2ag-hadoop-01.u-ga.fr:8088/proxy/application_1605490088936_0045/
2020-11-16 16:01:05,845 INFO mapreduce.Job: Running job: job_1605490088936_0045
2020-11-16 16:01:11,945 INFO mapreduce.Job: Job job_1605490088936_0045 running in uber mode : false
2020-11-16 16:01:11,946 INFO mapreduce.Job:  map 0% reduce 0%
2020-11-16 16:01:17,008 INFO mapreduce.Job: Task Id : attempt_1605490088936_0045_m_000000_0, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
     at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:325)
     at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:538)
     at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
     at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
     at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
     at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:465)
     at org.apache.hadoop.mapred.MapTask.run(MapTask.java:349)
     at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:174)
     at java.security.AccessController.doPrivileged(Native Method)
     at javax.security.auth.Subject.doAs(Subject.java:422)
     at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1729)
     at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:168)

2020-11-16 16:01:17,023 INFO mapreduce.Job: Task Id : attempt_1605490088936_0045_m_000001_0, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
     at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:325)
     at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:538)
     at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
     at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
     at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
     at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:465)
     at org.apache.hadoop.mapred.MapTask.run(MapTask.java:349)
     at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:174)
     at java.security.AccessController.doPrivileged(Native Method)
     at javax.security.auth.Subject.doAs(Subject.java:422)
     at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1729)
     at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:168)

2020-11-16 16:01:21,057 INFO mapreduce.Job: Task Id : attempt_1605490088936_0045_m_000001_1, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
     at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:325)
     at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:538)
     at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
     at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
     at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
     at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:465)
     at org.apache.hadoop.mapred.MapTask.run(MapTask.java:349)
     at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:174)
     at java.security.AccessController.doPrivileged(Native Method)
     at javax.security.auth.Subject.doAs(Subject.java:422)
     at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1729)
     at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:168)

2020-11-16 16:01:22,064 INFO mapreduce.Job: Task Id : attempt_1605490088936_0045_m_000000_1, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
     at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:325)
     at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:538)
     at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
     at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
     at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
     at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:465)
     at org.apache.hadoop.mapred.MapTask.run(MapTask.java:349)
     at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:174)
     at java.security.AccessController.doPrivileged(Native Method)
     at javax.security.auth.Subject.doAs(Subject.java:422)
     at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1729)
     at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:168)

2020-11-16 16:01:26,088 INFO mapreduce.Job: Task Id : attempt_1605490088936_0045_m_000001_2, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
     at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:325)
     at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:538)
     at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
     at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
     at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
     at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:465)
     at org.apache.hadoop.mapred.MapTask.run(MapTask.java:349)
     at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:174)
     at java.security.AccessController.doPrivileged(Native Method)
     at javax.security.auth.Subject.doAs(Subject.java:422)
     at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1729)
     at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:168)

2020-11-16 16:01:26,090 INFO mapreduce.Job: Task Id : attempt_1605490088936_0045_m_000000_2, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
     at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:325)
     at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:538)
     at org.apache.hadoop.streaming.PipeMapper.close(PipeMapper.java:130)
     at org.apache.hadoop.mapred.MapRunner.run(MapRunner.java:61)
     at org.apache.hadoop.streaming.PipeMapRunner.run(PipeMapRunner.java:34)
     at org.apache.hadoop.mapred.MapTask.runOldMapper(MapTask.java:465)
     at org.apache.hadoop.mapred.MapTask.run(MapTask.java:349)
     at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:174)
     at java.security.AccessController.doPrivileged(Native Method)
     at javax.security.auth.Subject.doAs(Subject.java:422)
     at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1729)
     at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:168)

2020-11-16 16:01:32,126 INFO mapreduce.Job:  map 100% reduce 100%
2020-11-16 16:01:32,132 INFO mapreduce.Job: Job job_1605490088936_0045 failed with state FAILED due to: Task failed task_1605490088936_0045_m_000001
Job failed as tasks failed. failedMaps:1 failedReduces:0 killedMaps:0 killedReduces: 0

2020-11-16 16:01:32,217 INFO mapreduce.Job: Counters: 14
     Job Counters
          Failed map tasks=7
          Killed map tasks=1
          Killed reduce tasks=1
          Launched map tasks=8
          Other local map tasks=6
          Rack-local map tasks=2
          Total time spent by all maps in occupied slots (ms)=24705
          Total time spent by all reduces in occupied slots (ms)=0
          Total time spent by all map tasks (ms)=24705
          Total vcore-milliseconds taken by all map tasks=24705
          Total megabyte-milliseconds taken by all map tasks=49410000
     Map-Reduce Framework
          CPU time spent (ms)=0
          Physical memory (bytes) snapshot=0
          Virtual memory (bytes) snapshot=0
2020-11-16 16:01:32,218 ERROR streaming.StreamJob: Job not successful!
Streaming Command Failed!

```

### 4.2 Combiner

>Pouvez-vous utiliser directement le reducer de la question précédente comme combiner ? Pourquoi ?

On ne peut pas utiliser le reducer pour deux raisons:

* la sortie du réducer n'est pas de type cle valeur , mais cle liste de valeur, il faut pouvoir les grouper par cle.
* la sortie du réducer renvoye les k meilleurs et comme le combiner est lancé sur chaque noeud mapper, celui-ci reverrait les k meilleurs localement sur le résultat d'un mapper. Ce résultat ne correspondrait pas au résultat attendu.

>Réfléchissez à l’entrée et à la sortie du combiner. Écrivez le combiner et modifiez le reducer de la question précédente pour que le résultat soit correct.

Assumons que chaque mapper revoie une liste cle, valeur : <pays,hashtag>
Le combiner construit une cle, valeur de type <pays, listhashtag> avec listhashtag (hashtag1,hashtag2..).  
Le reducer construit une liste pour chaque pays de l'ensemble des hashtags en sortie des réducers

#### combiner_flick.py

```python
#!/usr/bin/env python

import os
import sys
import json
k=4
def combiner_file(afile):
    assert(os.path.isfile(afile)), "file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return combiner(f)



def get_list_tag_by_country(data):
    """
    for each contry build list of tag
    """
    data_dict = dict()
    for line in data:
        if line.strip():
            line = line.strip().split('\t')
            # line contain country tag values
            if len(line) == 2:
                # create a dict of list of tag
                country = line[0]
                if country in data_dict:
                    data_dict[country].append(line[1])
                else:
                    data_dict[country] = [line[1]]
    return data_dict

def combiner(data):
    data_dict = get_list_tag_by_country(data)
    return '\n'.join(["\t".join([key, "\t".join(val)]) for key, val in data_dict.items()])


if __name__ == "__main__":
    print(combiner(sys.stdin) )
    #print(combiner_file("out_mapper_flickr.txt"))

```

#### reducer_flickr_with_combiner.py

```python
#!/usr/bin/env python

import os
import sys
import json
k=4
def reducer_file(afile):
    assert(os.path.isfile(afile)), "file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return reducer(f)


def get_list_best_tag_by_country (data_dict):
    """
    take a list of tag by contry return only k best tags by contry
    """
    res_dict = dict()
    for  country, tags in data_dict.items():
        # get all tag for contry
        lst_tag = list(dict.fromkeys(tags))
        nb_val_tag = [None] * len(lst_tag)
        for i in range(len(lst_tag)):
            nb_val_tag[i]=tags.count(lst_tag[i])
        sorted_lst_tag = [x for _,x in sorted(zip(nb_val_tag,lst_tag), reverse=True)]
        #take k first one
        res_dict[country] = ' '.join(sorted_lst_tag[:4])
    return res_dict

def get_list_tag_by_country(data):
    """
    for each contry build list of tag
    """
    data_dict = dict()
    for line in data:
        if line.strip():
            line = line.strip().split('\t')
            # line contain country tag list values
            if len(line) >= 2:
                # create a dict of list of tag
                country = line[0]
                if country in data_dict:
                    data_dict[country]= data_dict[country] +line[1:]
                else:
                    data_dict[country] = []+line[1:]
    return data_dict

def reducer(data):
    data_dict = get_list_tag_by_country(data)
    res_dict = get_list_best_tag_by_country(data_dict)
    return '\n'.join(["\t".join([key, str(val)]) for key, val in res_dict.items()])


if __name__ == "__main__":
    print(reducer(sys.stdin) )
    #print(reducer_file("out_mapper_flickr.txt"))

```

>Question : la structure de données utilisée dans le reducer contient l’ensemble des tags de l’ensemble des pays.  
Cela peut-il poser un problème pour traiter de grands volumes de données ?

A l'entrée du reducer les étapes de "Shuffle & Sort" permettent de répartir les traiements sur plusieurs reducers en fonction des clés.  
Neanmoins, si le nombre de reducer ou la répartions par clée n'est pas assez discriminante, et qu'un trop grand nombre de valeurs sont envoyées au même réducer en même temps, il se peut que cela pose un problème au réducer, puisque celui-ci gère la liste en mémoire.  
En python la taille maximale d'une liste est de 536 870 912 elements sur un système 32 bits, deplus il faut que la RAM soit suffisament grande pour contenit un tel nombre de valeurs.
