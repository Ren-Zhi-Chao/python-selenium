#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from util.ConfigParser import ConfigParser
import xlrd
from domain.Core import MyWebDrive, BROWSER_OPETION, OTHER_OPETION, ELEMENT_OPETION
from util.TimeUtil import getTime, DATE_FORMATE
config = ConfigParser()
output = config.fileOutput()
# from selenium import webdriver

# from util.TimeUtil import *
# from util.ConfigParser import ConfigParser

# DRIVE = {
# 	'chrome': 'Chrome'
# }

# class MyWebdriver:
# 	browser = None
# 	def __init__(self, drive_type = DRIVE['chrome'], load_timeout = 300):
# 		if 'Chrome' == drive_type:
# 			self.browser = webdriver.Chrome()
# 		self.setOutTime(load_timeout)
# 		#self.page_source
		
# 	def setOutTime(self, timeout):
# 		self.browser.set_page_load_timeout(timeout)
	
# 	def OpenBrowser(self, url):
# 		attempt = 1
# 		print('%s 第 [%d] 尝试连接【%s】站点'%(getNow(), attempt, url))
# 		self.browser.get(url)
# 		print(self.browser)
		
		
# myWD = MyWebdriver(drive_type = 'Chrome')
# myWD.OpenBrowser('http://www.baidu.com')
EXCEL = {
	"browser": {
		"valid": ['open', 'resize', 'back', 'forward', 'refresh', 'close', 'quit'],
		"func": BROWSER_OPETION
	},
	"other": {
		"valid": ['wait'],
		"func": OTHER_OPETION
	},
	"element": {
		"valid": ['clear', 'set', 'clear&set'],
		"func": ELEMENT_OPETION
	}
}

def fun_isdigit(val):
	try:
		return int(float(val))
	except:
		return ''

# 行处理
def sheet_handle(driver, row_value, output = None):
	print(row_value)
	xh = int(row_value[0])
	type = row_value[3].lower()
	seletor = row_value[4].lower()
	optn = row_value[5].lower()
	express = row_value[6].lower()
	value = str(row_value[7]).lower()
	wait_time = str(row_value[8]).strip()
	wait_time = fun_isdigit(wait_time)
	save_image = row_value[9]
	skip = row_value[10]
	if skip:
		return
	if not type in EXCEL:
		print('...元素类型选择错误.....')
		return
	if not (optn in EXCEL[type]['valid']):
		print('...选择的类型不正确.....')
		return
	funKey = None
	if 'browser' == type or 'other' == type:
		funKey = optn
	else:
		funKey = seletor
	EXCEL[type]['func'][funKey](driver, 
		value = value, optn = optn, wait_time = wait_time,
		express = express, seletor = seletor)
	if save_image:
		file_output = output + os.sep + str(int(xh)) + '.png'
		print(' => 页面截图: %s'%file_output)
		driver.get_screenshot_as_file(file_output)
	print('方法结束..')

if __name__ == "__main__":
	config = ConfigParser()
	file_path = config.filePath() + os.sep + config.fileName()
	if not os.path.exists(file_path):
		print(' ERROR: 文件不存在! %s'%file_path)
	else:
		workbook = xlrd.open_workbook(file_path)
		sheet_datas = workbook.sheets()
		driver = MyWebDrive().GetDrive(config.driveType())
		for sheet in sheet_datas:
			if sheet.name.startswith('script'):
				if output:
					output = output + getTime(DATE_FORMATE['DIR']) + os.sep + sheet.name + os.sep
					if not os.path.exists(output):
						os.makedirs(output)
				# print(sheet.nrows, sheet.ncols)
				for i in range(sheet.nrows):
					if i > 0:
						print('当前操作第[%d]行'%i)
						sheet_handle(driver, sheet.row_values(i), output = output)