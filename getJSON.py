
from pymongo import MongoClient
from random import randint
import os
import time
import argparse
import json
import CommonCode as cc
import pprint

def GetDict(dataDict, name='duts'):

    statDict={}

    for k, v in dataDict.items():
        statDict[str(k)]=str(v)

    return statDict

##################################
# Main
##################################

def main():

    argDict=cc.GetDBArgs()
    print('argDict: '+str(argDict))

    collection=cc.GetCollection(argDict['database'], argDict['collection'])


    print('total record for the collection: ' + str(collection.count()))
    #Step 3: a)find files and b)translate stats
    myPosts = collection.find()

    outFileName='outFile_'+argDict['database']+'_'+argDict['collection']+'.txt'
    outFile=open(outFileName, 'w')
    outFile.close()


    count=0
    for p in collection.find():
        print('\n\n')
        outDict=GetDict(p)
        print(outDict)
        with open(outFileName, 'a') as outfile:
            json.dump(outDict,outfile)
        count+=1
    print('finished reading {0} datarate entries'.format(count))


if __name__ == "__main__":
    print('### in '+str(__file__)+' ###')
    start = time.time()
    main()
    end = time.time()
    print('\n+++ Total time: '+str(end-start)+'seconds +++\n')
    print('### out '+str(__file__)+' ###')
