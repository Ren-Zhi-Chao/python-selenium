#! /usr/bin/env python
# -*- coding: utf-8 -*-
from util.ConfigParser import ConfigParser
import os, zipfile, platform
from util.DownLoadUtil import Downloadprogress as Download

cofig = ConfigParser()

__DRIVE_EXPLAIN = {
	"chrome": {
		"uri": "https://npm.taobao.org/mirrors/chromedriver/%s/chromedriver_%s.zip"
	}
}

__SYSTEM = {
	"Windows": "win32"
}

def Chrome(type, version):
	print(' => 已选择谷歌浏览器进行测试，正在检查驱动配置....')
	print(' => 检查环境变量: BROWSER_DIVER_CHROME')
	env = os.environ.get('BROWSER_DIVER_CHROME')
	isDownload = True
	if env:
		print(' √ 已检测到地址: %s'%(env))
		print(' => 检查驱动是否存在....')
		if os.path.exists(env + os.sep + 'chromedriver.exe'):
			isDownload = False
			print(' √ 检测环境已配置完毕，如果仍有问题检查驱动版本是否一致，或可将环境变量删除使用本程序下载！')
	if isDownload:
		print(' × 驱动配置不正确....')
		print(' => 准备下载驱动程序....')
		uri = __DRIVE_EXPLAIN[type]['uri']%(version, __SYSTEM[platform.system()])
		print('    => 正在请求 【%s】'%(uri))
		filePath = Download(uri, savePath = os.getcwd(), name = 'chromedriver_win32', type = 'zip')
		print(' √ 下载完成：%s'%(filePath))
		zfile_path = os.getcwd() + os.sep + 'driver_chrome_%s'%(version)
		print(' => 解压压缩包...')
		zfile = zipfile.ZipFile(filePath, 'r')
		for fileM in zfile.namelist():
			zfile.extract(fileM, zfile_path)
		zfile.close()
		print(' √ 解压完成，解压地址: %s'%(zfile_path))
		print(' => 删除chromedriver_win32.zip')
		os.remove(filePath)
		print(' => 配置环境变量...')
		# os.putenv('BROWSER_DIVER_CHROME', zfile_path)
		# os.putenv('path', '%BROWSER_DIVER_CHROME%')
		print(' √ 已更新环境变量: BROWSER_DIVER_CHROME: %s'%(zfile_path))
		print(' 浏览器驱动已安装完毕，关闭此窗口运行start.py文件可执行自动化测试，如有问题，可执行help.yp查看帮助 ')
		print(' 如浏览器打开异常，可检查环境变量是否已生效，仍不好用检查驱动版本与浏览器是否对应 ')

BrowserDiverValid = {
	"chrome": Chrome
}

if __name__ == "__main__":
	driveType = cofig.driveType()
	version = cofig.driveVersion()
	BrowserDiverValid[driveType](driveType, version)
	print(cofig.filePath())
