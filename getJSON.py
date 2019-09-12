
from pymongo import MongoClient
from random import randint
import os
import time
import argparse
import json
import CommonCode as cc

##################################
# Main
##################################

def main():

    argDict=cc.GetDBArgs()
    print('argDict: '+str(argDict))

    collection=cc.GetCollection(argDict['database'], argDict['collection'])

    #Step 3: a)find files and b)translate stats
    myPosts = collection.find({'author': 'Scott'})

    count=0
    for p in myPosts:
        print(p)
        count+=1
    print('finished reading {0} datarate entries'.format(count))


if __name__ == "__main__":
    print('### in '+str(__file__)+' ###')
    start = time.time()
    main()
    end = time.time()
    print('\n+++ Total time: '+str(end-start)+'seconds +++\n')
    print('### out '+str(__file__)+' ###')
