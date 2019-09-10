
import myDetails
myDeets= myDetails.SetMondoDB()

from pymongo import MongoClient
from random import randint
import os
import time
import argparse
import CommonCode as cc

def GetJSON(fileName):

    statDict={}
    names=[]
    vals=[]

    with open(argDict['file']) as json_file:
        data = json.load(json_file)
        for p in data['DUT']:
            for k,v in p.iteritems()::
                try:
                    statDict[n]=int(v)
                except:
                    try:
                        statDict[n]=float(v)
                    except:
                        statDict[n]=v

    return statDict

##################################
# Main
##################################

def main():

    argDict=cc.GetDBArgs()
    print "argDict:",argDict

    collection=cc.SetCollectionArg(argDict)

    #Step 3: a)find files and b)translate stats

    ### a)
    myFiles= cc.GetFiles(argDict['path'], argDict['ext'])

    ### b)
    count=0
    for f in myFiles:
        print "working on:",f
        fileInfo= GetJSON(f)
        print fileInfo

        #Step 4: Insert object directly into MongoDB via insert_one
        result=collection.insert_one(fileInfo)
        count+=1
        ### Print to the console the ObjectID of the new document
        print('Created {0} entry as {1}'.format(count,result.inserted_id))
        if argDict['max']>0 and count>=argDict['max']: break
    #Step 5: Tell us that you are done
    print('finished creating {0} datarate entries'.format(count))


if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"
