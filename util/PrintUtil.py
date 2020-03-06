#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, time, math

class ProgressBar:
	def __init__(self, count = 0, total = 0, width = 50, progress = True, console = True):
		self.count = count
		self.total = total
		self.width = width
		self.progress = progress
		self.console = console
	def move(self):
		self.count += 1
		return self
	def log(self, **arg):
		sys.stdout.write(' ' * (self.width + 9) + '\r')
		sys.stdout.flush()
		if self.console == True:
			if 'show' in arg:
				print(arg['show'])
			sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
		if self.progress == True:
			progress = self.width * self.count / self.total
			right = str('').rjust(int(progress), '#')
			lack = str('').rjust(math.ceil(self.width - progress), '-')
			sys.stdout.write(right + lack + '\r')
			if progress == self.width:
				sys.stdout.write('\n')
		sys.stdout.flush()
		return self

if __name__ == '__main__':
	bar = ProgressBar(total = 10, progress = False)
	for i in range(10):
		bar.move().log()
		time.sleep(1)