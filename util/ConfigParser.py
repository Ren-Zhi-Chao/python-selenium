#! /usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os

class ConfigParser:
    def __init__(this, filePath = os.getcwd() + os.sep + 'config' + os.sep + 'config.ini'):
        this.fp = filePath
        this.conf = configparser.ConfigParser()
        this.conf.read(this.fp, encoding="utf-8-sig")
    def driveType(this):
        return this.conf.get('drive', 'type').lower().strip()
    def driveVersion(this):
        return this.conf.get('drive', 'version').strip()

    def filePath(this):
        file_path = this.conf.get('file', 'path').strip()
        return file_path if len(file_path) > 0 else os.getcwd() + os.sep + 'script'
    def fileName(this):
        file_name = this.conf.get('file', 'name').strip()
        return file_name if len(file_name) > 0 else ''
    def fileOutput(this):
        output = this.conf.get('file', 'output').strip()
        if not output:
            output = os.getcwd() + os.sep + 'output' + os.sep
        elif 'false' == output:
            return False
        return output

    def WinSize(this):
        return this.conf.get('window', 'size').strip()
    def WinFrequency(this):
        poll_frequency = this.conf.get('window', 'frequency').strip()
        return poll_frequency if len(str(poll_frequency)) > 0 else 0.5
    def WinImplicitly(this):
        return this.conf.get('window', 'implicitly').strip()
        
    def PlugsFile(this):
        return this.conf.get('plugs', 'filepath').strip()

if __name__ == '__main__':
    ConfigParser().filePath()