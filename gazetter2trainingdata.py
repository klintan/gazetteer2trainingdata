#!/usr/bin/python
import os, sys
import MySQLdb
#import Stemmer

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="simplyfai") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

#tried stemming but didn't work
#stemmer = Stemmer.Stemmer('swedish')

# Use all the SQL you like

# print all the first cell of all the rows
#for row in cur.fetchall() :
#    print row[0]

#Implement a search where we have two or more labels in a row we will search the full entity
# including both the labels that are concurrent
#
#


f1 = open("output_training.txt", "a")
sentence = []
train_sentence = []

doc = []
old_arr = ['', '']
with open (sys.argv[1], "r") as f:
    for idx, line in enumerate(f):
        arr = line.split('\t')
        #print arr

        if (arr[1]=='LABEL\n'):
            #print arr[1]
            #temp_word = stemmer.stemWord(arr[0])
            #print temp_word

            cur.execute("SELECT label FROM gazetters WHERE gazette='%s'"%arr[0])
            for row in cur:
                arr[1] = row[0]+"\n"

            print cur.rowcount
            if (cur.rowcount==0 and arr[0][-1] == 's'):
                cur.execute("SELECT label FROM gazetters WHERE gazette='%s'"%arr[0][:-1])
                for row in cur:
                    arr[1] = row[0]+"\n"

        if(old_arr[1] == 'LABEL\n' and arr[1] == 'LABEL\n')
            cur.execute("SELECT label FROM gazetters WHERE gazette='%s'"%arr[0] + ' ' + old_arr[0])
            for row in cur:
                arr[1] = row[0]+"\n"

        #for row in cur.fetchon():
         #  print row[0]
         #  line[1] = row[0]

        #if we have a consecutive multi-word entity, set all labels to same
        if((old_arr[1] == 'PER\n' or old_arr[1] == 'LOC\n' or old_arr[1] == 'ORG\n' or old_arr[1] == 'MISC\n') and arr[1] == 'LABEL\n'):
            arr[1] = old_arr[1]


        #if (arr_old[1] != '0\n' and arr_old[1] != 'LABEL'):
            #print "should be the same"
            #print arr_old[1]
            #print arr[1]
            #arr[1] = arr_old[1]

        doc.append("\t".join(arr))
        if len(doc) == 500:
            f1.write("".join(doc))
            doc = []

        old_arr = arr


f1.write("".join(doc))
f1.close()