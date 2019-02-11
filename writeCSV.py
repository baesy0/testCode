#!/usr/bin/env python
#coding:utf8

import csv

with open('test0.csv', mode = 'w') as csv_file:
	fieldnames = ['ep', 'seq', 'scene', 'shot', 'note']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'ep':'1', 'seq':'CAR', 'scene':'FOO', 'shot':'0010', 'note':'cg car'})
	writer.writerow({'ep':'1', 'seq':'CAR', 'scene':'FOO', 'shot':'0020', 'note':'add dust'})
	writer.writerow({'ep':'1', 'seq':'CAR', 'scene':'BAR', 'shot':'0010', 'note':'cg car, add dust'})
