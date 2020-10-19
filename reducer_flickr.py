#!/usr/bin/env python

import os
import sys
import numpy as np
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
        res_dict[country] = ' '.join(sorted_lst_tag[:k])
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
                    data_dict[line[0]].append(line[1])
                else: 
                    data_dict[line[0]] = [line[1]]
    return data_dict

def reducer(data):
    data_dict = get_list_tag_by_country(data)
    res_dict = get_list_best_tag_by_country(data_dict)
    return '\n'.join(["\t".join([key, str(val)]) for key, val in res_dict.items()])


if __name__ == "__main__":
    print(reducer(sys.stdin) )
    #print(reducer_file("out_mapper_flickr.txt"))
    