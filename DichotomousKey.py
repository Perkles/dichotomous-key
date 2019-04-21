"""
The MIT License (MIT)

Copyright (c) 2015 Ian Duncan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import csv

class DichotomousKey(object):
	def __init__(self, name=None, author=None, steps=[]):
		self.name = name
		self.author = author
		self.steps = steps

	def load(self, file_name):
		with open(file_name + '.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					self.unpack_list(row)
					line_count += 1
				else:
					self.unpack_list(row)
					line_count += 1

	def unpack_list(self, row):
		if len(row) == 4:
			level, argument, goto, animal = row
			return self.steps.append(Step(level, argument, goto, animal))
		else:
			level, argument, goto = row
			return self.steps.append(Step(level, argument, goto))

	def execute(self, level):
		print(self.steps[level].level + 'a : ' + self.steps[level].argument)
		print(self.steps[level + 1].level + 'b : ' + self.steps[level + 1].argument)
		choice = str(input('(a/b) > '))
		if choice == 'a':
			if self.steps[level].has_animal():
				print("Your animal is: %s" %(self.steps[level].animal))
			else:
				self.execute(self.steps[level].get_list_index(self.steps[level].goto))
		elif choice == 'b':
			if self.steps[level+1].has_animal():
				print("Your animal is: %s" %(self.steps[level+1].animal))
			else:
				self.execute(self.steps[level+1].get_list_index(self.steps[level+1].goto))

class Step(object):
	def __init__(self, level=None, argument=None, goto=None, animal=None):
		self.level = level
		self.argument = argument
		self.goto = goto
		self.animal = animal

	def has_animal(self):
		if self.animal:
			return True

	def get_list_index(self, goto):
			return (int(goto) * 2) - 2

d_key = DichotomousKey()
d_key.load('six_legs_well_dev_wings')
d_key.execute(0)