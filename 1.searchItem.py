#!/usr/bin/env python
#coding:utf8
import os

def searchItem(root):
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root+"/"+subdir):
			shot.append("/".join([root,subdir,f]))
		shot.sort()
		seqs.append(shot)
	return results seqs

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	print searchItem(root)
