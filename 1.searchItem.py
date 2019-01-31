#!/usr/bin/env python
#coding:utf8
import os

def searchItem(root):
	results = []
	for subdir in os.listdir(root):
		for f in os.listdir(root+"/"+subdir):
			results.append("/".join([root,subdir,f]))
			
	results.sort()
	return results

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	print searchItem(root)
