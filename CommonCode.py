
import myDetails
myDeets= myDetails.SetMondoDB()

from pymongo import MongoClient
from random import randint
import os
import time
import argparse

######################
### parsing
######################

def GetDBArgs(ad=None):

    parser = argparse.ArgumentParser(description="MongoDB tool")

    parser.add_argument('--mode', help='create/update/replace/delete')
    parser.add_argument('--database', help='database name')
    parser.add_argument('--collection', help='collection name')
    parser.add_argument('--path', help='path to stat files (default "/Users/kwraight/CERN_repositories/streamsim/testDir/")')
    parser.add_argument('--ext', help='extension of stat files (default ".txt")')
    parser.add_argument('--file', help='input stat json file (default "NYS")')
    parser.add_argument('--max', help='max number of entries to add to collection (default not set (-1))')
    parser.add_argument('--name', help='name (default not set)')

    args = parser.parse_args()

    print "args:",args

    argDict={}
    if ad==None:
        argDict={'mode':"NYS", 'file':"NYS", 'name':"NYS", 'database':"NYS", 'collection':"NYS", 'path':"/Users/kwraight/CERN_repositories/streamsim/testDir/", 'ext':".txt", 'max':-1}
    else:
        argDict=ad

    for a in vars(args).iteritems():
        if not a[1]==None:
            print "got argument",a
            try:
                argDict[a[0]]=int(a[1])
            except:
                argDict[a[0]]=a[1]

    return argDict

##################################
# Useful Functions
##################################

def GetFiles(path,ext):

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if ext in file:
                files.append(os.path.join(r, file))
    print "Found",len(files),"in",path

    return files


def CheckDatabase(dnName, mdbClient):

    retStatus=False

    db_names=[]
    if len(mdbClient.database_names()) == 0:
        #print('bugger all databases in client')
        retStatus=False
    else:
        db_names=[ dn.encode('ascii') for dn in mdbClient.database_names()]
        #print(db_names)

    if dnName in db_names:
        #print('found database: {0}'.format(argDict['database']))
        retStatus=True

    return retStatus


def CheckCollection(colName, database):

    retStatus=False

    col_names=database.collection_names()
    if len(col_names) == 0:
        print('bugger all collections in database')
        retStatus=False

    if colName in col_names:
        retStatus=True

    return retStatus


def SetClient():

    client = MongoClient("mongodb+srv://"+myDeets.username+":"+myDeets.password+"@cluster0-yrb5p.mongodb.net/test?retryWrites=true&w=majority")

    return client

def GetCollection(dnName, colName):

    #Step 1: Connect to MongoDB - Note: Change connection string as needed
    mdbClient = SetClient()

    #Step 2: Check if a)database and b)collection exist
    ### a)
    if CheckDatabase(dnName, mdbClient):
        print('found database: {0}'.format(dnName))
    else:
        print('No such database found: {0}'.format(dnName))

    db = mdbClient[dnName]

    ### b)
    if not CheckCollection(colName, db):
        print('No such collection found: {0}'.format(colName))
    else:
        print('found collection: {0}'.format(colName))

    collection = db[colName]

    return collection


def SetCollection(dnName, colName, mode="NYS"):

    if "NYS" in mode:
        print('\n!!! Unspecified mode. Please define: create/update/replace/delete')
        return

    #Step 1: Connect to MongoDB - Note: Change connection string as needed
    mdbClient = SetClient()

    #Step 2: Check if a)database and b)collection exist
    ### a)
    if CheckDatabase(dnName, mdbClient):
        print('found database: {0}'.format(dnName))
    else:
        print('No such database found: {0}'.format(dnName))

        if "create" in mode.lower():
            print('will create database: {0}'.format(dnName))
        else: return

    db = mdbClient[dnName]

    ### b)
    if not CheckCollection(colName, db):
        print('No such collection found: {0}'.format(colName))
        if "create" in mode.lower():
            print('will create collection: {0}'.format(colName))
        else: return
    else:
        print('found collection: {0}'.format(colName))

    if "replace" in mode.lower() or "delete" in mode.lower():
        db[colName].drop()

        if "delete" in mode.lower(): return

    if "update" in mode.lower():
        print('will update collecion: {0}'.format(colName))

    collection = db[colName]

    return collection

def SetCollectionArg(argDict):
    print("argDict: ",str(argDict))

    if "NYS" in argDict['mode']:
        print('\n!!! Unspecified mode. Please define: create/update/replace/delete')
        return

    #Step 1: Connect to MongoDB - Note: Change connection string as needed
    client = MongoClient("mongodb+srv://"+myDeets.username+":"+myDeets.password+"@cluster0-yrb5p.mongodb.net/test?retryWrites=true&w=majority")

    #Step 2: Check if a)database and b)collection exist

    ### a)
    db_names=[]
    if len(client.database_names()) == 0:
        print('bugger all databases in client')
        return
    else:
        db_names=[ dn.encode('ascii') for dn in client.database_names()]
        print(db_names)

    if argDict['database'] in db_names:
        print('found database: {0}'.format(argDict['database']))
    else:
        print('No such database found: {0}'.format(argDict['database']))

        if "create" in argDict['mode']:
            print('will create database: {0}'.format(argDict['database']))
        else: return

    db = client[argDict['database']]

    ### b)
    col_names=db.collection_names()
    if len(col_names) == 0:
        print('bugger all collections in database')
        if "create" in argDict['mode']:
            print('will create collection: {0}'.format(argDict['collection']))
        else: return

    if argDict['collection'] in col_names:
        print('found collection: {0}'.format(argDict['collection']))
    else:
        print('No such collection found: {0}'.format(argDict['collection']))

        if "create" in argDict['mode']:
            print('will create collecion: {0}'.format(argDict['collection']))
        else: return

    if "replace" in argDict['mode'] or "delete" in argDict['mode']:
        db[argDict['collection']].drop()

        if "delete" in argDict['mode']: return

    if "update" in argDict['mode']:
        print('will update collecion: {0}'.format(argDict['collection']))

    collection = db[argDict['collection']]

    return collection
