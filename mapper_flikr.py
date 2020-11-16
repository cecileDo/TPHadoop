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
