#!/usr/bin/env python
#coding:utf8
import argparse

parser = argparse.ArgumentParser(description = 'description', epilog = 'epilog')

parser.add_argument("-p", "--project", help = "project name")
parser.add_argument("-s", "--shot", help = "shot name")
parser.add_argument("-u", "--user", help = "user name")
parser.add_argument("-t", "--task", help = "task name")

args = parser.parse_args()

print(args.project)
print(args.shot)
print(args.user)
print(args.task)
