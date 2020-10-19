#!/usr/bin/env python

import os
import sys
import numpy as np
import json

def reducer_file(afile):
    assert(os.path.isfile(afile)), "file %s doesnt exist"%afile
    with open(afile, 'r') as f:
        return reducer(f)

#!/usr/bin/env python3.6
def reducer(data):
    data_dict = dict()
    for line in data:
        if line.strip():
            word = line.strip().split(' ')
            if len(word) == 2:
                print (word)
                print (data_dict.get(word[0],0))
                print(word[1:])
                for val in word[1:]:
                    data_dict[word[0]] = data_dict.get(word[0],0)+ int(val)
    return '\n'.join([" ".join([key, str(val)]) for key, val in data_dict.items()])

if __name__ == "__main__":
    print(reducer(sys.stdin) )
    #print(reducer_file("out_mapper.txt"))