
from pymongo import MongoClient
from random import randint
import os
import time
import argparse
import json
import CommonCode as cc

def GetJSON(fileName, name='DUT'):

    statArr=[]
    names=[]
    vals=[]

    with open(fileName) as json_file:
        data = json.load(json_file)
        try:
            for p in data[name]:
                statArr.append(p)
        except KeyError:
            print('no key found matching: '+name)
        except:
            print('problem reading file')

    return statArr

##################################
# Main
##################################

def main():

    argDict=cc.GetDBArgs()
    print('argDict: '+str(argDict))

    collection=cc.SetCollection(argDict['database'], argDict['collection'], argDict['user'], argDict['mode'])

    #Step 3: a)find files and b)translate stats

    ### a)
    myFiles=[]
    if "NYS" in argDict['file']:
        myFiles= cc.GetFiles(argDict['path'], argDict['ext'])
    else:
        myFiles.append(argDict['file'])
    print('files found: '+str(len(myFiles)))

    ### b)
    count=0
    for f in myFiles:
        print('working on: '+f)
        #fileInfo= GetJSON(f, argDict['name'])
        with open(f) as dataFile:
            fileInfo = json.load(dataFile)
        print(fileInfo)

        #Step 4: Insert object directly into MongoDB via insert_one
        retArr=GetJSON(f,argDict['name'])
        if len(retArr)<0:
            print('no data returned from file: maybe check name')
            continue

        for ra in retArr:
            try:
                result=collection.insert_one(ra)
                ### Print to the console the ObjectID of the new document
                print('Created {0} entry as {1}'.format(count,result.inserted_id))
                count+=1
                if argDict['max']>0 and count>=argDict['max']: break
            except AttributeError:
                print('a problem with client. check mode: create/replace/update')
            except:
                print('a problem with client.')
    #Step 5: Tell us that you are done
    print('finished creating {0} datarate entries'.format(count))


if __name__ == "__main__":
    print('### in '+str(__file__)+' ###')
    start = time.time()
    main()
    end = time.time()
    print('\n+++ Total time: '+str(end-start)+'seconds +++\n')
    print('### out '+str(__file__)+' ###')
