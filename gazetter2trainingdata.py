#!/usr/bin/python
import os, sys
import MySQLdb
import Stemmer

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="db") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

#tried stemming but didn't work
stemmer = Stemmer.Stemmer('swedish')

# Use all the SQL you like

# print all the first cell of all the rows
#for row in cur.fetchall() :
#    print row[0]

f1 = open("output_training.txt", "a")
sentence = []
train_sentence = []

doc = []
with open (sys.argv[1], "r") as f:
    for line in f:
        arr = line.split('\t')
        #print arr

        if (arr[1]=='LABEL\n'):
            #print arr[1]
            #temp_word = stemmer.stemWord(arr[0])
            #print temp_word

            cur.execute("SELECT label FROM gazetters WHERE gazette='%s'"%arr[0])

            for row in cur:
                print(row)
                arr[1] = row[0]+"\n"

        #for row in cur.fetchon():
         #   print row[0]
          #  line[1] = row[0]

        doc.append("\t".join(arr))
        if len(doc) == 500:
            f1.write("".join(doc))
            doc = []

f1.write("".join(doc))
f1.close()