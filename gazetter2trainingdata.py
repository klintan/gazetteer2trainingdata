#!/usr/bin/python
import os, sys
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="yourdb") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM gazetters WHERE gazette='Andreas'")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]