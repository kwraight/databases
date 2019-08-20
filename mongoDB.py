
import myDetails
myDeets= myDetails.SetMondoDB()

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://"+myDeets.username+":"+myDeets.password+"@cluster0-yrb5p.mongodb.net/test?retryWrites=true&w=majority")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
