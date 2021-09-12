#!/usr/bin/python
import csv
import random as r

records=9000
print("Making %d records\n" % records)

fieldnames=['id','name','age','city']
writer = csv.DictWriter(open("people.csv", "w"), fieldnames=fieldnames)

names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
cities=['Delhi', 'Kolkata', 'Chennai', 'Mumbai']
print(r.random())
writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('id', i),
    ('name', r.random()),
    ('age', r.random()),
    ('city', r.random())]))