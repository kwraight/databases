
import myDetails
myDeets= myDetails.SetMondoDB()

from pymongo import MongoClient
#include pprint for readabillity of the
from pprint import pprint

#change the MongoClient connection string to your MongoDB database instance
client = MongoClient("mongodb+srv://"+myDeets.username+":"+myDeets.password+"@cluster0-yrb5p.mongodb.net/test?retryWrites=true&w=majority")
db=client.business

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)
