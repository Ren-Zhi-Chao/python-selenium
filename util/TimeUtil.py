#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

DATE_FORMATE = {
	'DATETIME': '%Y-%m-%d %H:%M:%S',
	'NO': '%Y%m%d%H%M%S',
	'DIR': '%Y-%m-%d %H%M%S'
}

def getTime(formate):
	return time.strftime(formate, time.localtime(time.time()))
	
def getUUID(**arg):
	num = 'X'
	length = 4
	just = '0'
	if 'num' in arg:
		num = str(arg['num'])
	if 'length' in arg:
		length = arg['length']
	if 'just' in arg:
		just = arg['just']
	if len(just) > 1:
		just = '0'
	if len(num) > length:
		length = len(num)
	return '%s%s'%(getTime(DATE_FORMATE['NO']), str(num).rjust(length, just))

def getNow(show = False):
	time = getTime(DATE_FORMATE['DATETIME'])
	if show == True:
		print(time)
	return time
