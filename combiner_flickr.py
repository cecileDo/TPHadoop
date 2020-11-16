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
    
