### test comminucation with database

from random import randint
import os
import time
import argparse
import CommonCode as cc

##################################
# Main
##################################

def main():

    testInfoA={'this':"that", 'here':1, 'there':[1,2,3]}
    testInfoB={'this':"what", 'here':2, 'there':[4,5,6]}
    testInfoC={'this':"taht", 'here':-3, 'there':[-9,-8,-7]}

    collection=cc.SetCollection("Jeremy", "Bearimy", mode="create")
    result=collection.insert_one(testInfoA)
    raw_input("did create work?")

    collection=cc.SetCollection("Jeremy", "Bearimy", mode="update")
    result=collection.insert_one(testInfoB)
    raw_input("did update work?")

    collection=cc.SetCollection("Jeremy", "Bearimy", mode="replace")
    result=collection.insert_one(testInfoC)
    raw_input("did replace work?")

    collection=cc.SetCollection("Jeremy", "Bearimy", mode="delete")
    raw_input("did delete work?")

    #Step 3: a)find files and b)translate stats


if __name__ == "__main__":
    print "### in",__file__,"###"
    start = time.time()
    main()
    end = time.time()
    print "\n+++ Total time: ",(end-start),"seconds +++\n"
    print "### out",__file__,"###"
