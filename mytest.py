#!/usr/bin/env python
#coding:utf8
import os


def genThumb(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	if not os.path.exists("/usr/bin/convert"):
		return "ImageMagick이 설치되지 않았습니다."

	d, f = os.path.split(src)
	notuse, srcExt = os.path.splitext(f)
	dstExt = ".jpg"
	dst = d+"/"+f.replace(srcExt,dstExt)
	size = "360x240"
	cmd = "convert {src} -thumbnail {size} -background black -gravity center -extent {size} {dst}".format(
			src = src,
			dst = dst,
			size = size)
	os.system(cmd)
	
if __name__ == "__main__":
	path = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078950.exr"
	genThumb(path)
	


