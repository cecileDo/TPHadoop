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
    return  ('\t1 \n'.join(line)+'\t1\n')

if __name__ == "__main__":
    #print (mapper_file("data.txt") )
    print (mapper(sys.stdin) )