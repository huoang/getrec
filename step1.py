#!/usr/bin/env python
#ecoding:utf-8

from main import fulldata 
import re

#print fulldata[1:1000]
#print len(fulldata)

hosdata=map((lambda x:re.findall("41\\d{10}",x[45:75])),fulldata)





