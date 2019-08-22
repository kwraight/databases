# Databases

### Repository for python2 (python 3 later) tools to upload to databases

Templates for databases:
* [MongoDB](#mongodb)
  * at the moment based on-line only DB

---

# [MongoDB](https://cloud.mongodb.com)
Used for stream simulations on [gitlab](https://gitlab.cern.ch/wraight/streamsim)
* Basic tutorial:
https://www.sitepoint.com/getting-started-with-python-and-mongodb/
* Querying information:
https://docs.mongodb.com/manual/reference/operator/query/

## Upload csv file
Compare defined stream statistic across global positions
Five main steps:
1. Connect to MongoDB
2. Check if a)database and b)collection exist
3.  a)find files in path and b)Per file: translate stats to python dictionary
4. Per file: insert dictionary directly into MongoDB via insert_one
5. Tell us that you are done

**Command**
`dataSample.py`

| Args | Comment (default) | e.g. |
| --- | --- | --- |
| mode | mode of running: create/update/replace/delete (not set) | |
| database | database name (not set) | datarates |
| collection | collection name (not set) | chips |
| path | path to stat files ("/Users/kwraight/CERN_repositories/streamsim/testDir/") | |
| ext | extension of stat files (".txt") | |
| max | max number of entries to add to collection (not set(-1)) | |

*E.g.*
`python dataSample.py --database datarates --collection chipsX0pc --mode create --path /Users/kwraight/CERN_repositories/streamsim/testDir/`

**Comment**
