#!/usr/bin/env python
#coding:utf8
import os
import subprocess

proxyPath = "/tmp/proxy/jpg"

def genJPG(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	global proxyPath

	if not os.path.exists(src):
		return "파일이 존재하지 않습니다."
	if not os.path.exists("/usr/bin/convert"):
		return "ImageMagick이 설치되지 않았습니다."
	if not os.path.exists(proxyPath):
		return "경로가 존재하지 않습니다"
	
	exrs = os.listdir(src)
	exrs.sort()
	size = "360x240"
	
	for i in exrs:
		notuse, ext = os.path.splitext(i)
		dst = proxyPath+"/"+i.replace(ext, ".jpg")
		cmds = ["convert", src+"/"+i,"-thumbnail",size,
				"-background","black","-gravity","center",
				"-extent",size,dst]
		#print " ".join(cmds)	
		p = subprocess.Popen(cmds,
							stdout = subprocess.PIPE,
							stderr = subprocess.PIPE)
		#print p.communicate()[1]
		return None

	

if __name__ == "__main__":
	path = "/project/circle/in/aces_exr/A003C025_150830_R0D0"
	err = genJPG(path)
	if err:
		print err

#aces_exr 하위 폴더가 있는지 검사. 제일 하단 폴더의 파일들을 바꾸기.
