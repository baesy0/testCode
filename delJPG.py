#!/usr/bin/env python
#coding:utf8
import subprocess

def delJPG(path):
	"""
	지정된 경로의 proxy폴더를 삭제한다
	"""
	cmds = ["rm -rf", path+"/jpg"]



if __name__ == "__main__":
	proxyPath = "/tmp/proxy/jpg"
	delJPG(proxyPath)
