#!/usr/bin/env python
#coding:utf8
import ConfigParser

ini = ConfigParser.ConfigParser()
ini.read("data.ini")

print ini.sections()
print ini.options("project")
print ini.get("project", "name")
