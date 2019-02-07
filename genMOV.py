#!/usr/bin/env python
#coding:utf8
import os
import re
import subprocess

def genMOV(proxyPath):
	jpgFiles = os.listdir(proxyPath)
	startFrame = re.findall("(\d+)\.jpg", jpgFiles[0]).pop()
	endFrame = re.findall("(\d+)\.jpg", jpgFiles[-1]).pop()
	vframes = int(endFrame)-int(startFrame) + 1
	cmds=["/home/bae/app/ffmpeg/ffmpeg", "-y",
		"-f","image2",
		"-start_number", startFrame,
		"-r","24",
		"-i",proxyPath+"/"+"A003C025_150830_R0D0.%6d.jpg",
		"-vframes",str(vframes),
		"-vcodec", "libx264",
		#"-vf", "scale=1280:-1",
		"/tmp/output.mov"]
	#print jpgFiles
	#print " ".join(cmds)
	#cmd = " ".join(cmds)
	#os.system(cmd)
	p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print p.communicate()
		#start_number vframes 어떻게 가져오지



if __name__=="__main__":
	jpgPath = "/tmp/proxy/jpg"
	genMOV(jpgPath)
