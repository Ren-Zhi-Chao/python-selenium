#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from urllib.request import urlretrieve
from util.TimeUtil import getUUID as UUID
from util.PrintUtil import ProgressBar

def __reporthook(blocks_read, block_size, total_size):
    progressBar = ProgressBar(total = total_size, console = False)
    if not blocks_read:
        print('Connection opened.')
    if total_size < 0:
        print ('Read %d blocks'%(blocks_read))
    else:
        show = 'downloading: %d KB, totalsize: %d KB'%(blocks_read * block_size / 1024.0, total_size / 1024.0)
        progressBar.move().log(show = show)

def Download(url, savePath = os.getcwd(), name = UUID(), type = None):
    print(savePath, name, type)
    f = open(savePath + os.sep + '%s.%s'%(name, type))
    f.close()

def Downloadprogress(url, savePath = os.getcwd(), name = UUID(), type = None):
    file_path = savePath + os.sep + '%s.%s'%(name, type)
    print(file_path)
    urlretrieve(url, file_path, __reporthook)
    return file_path