import csv

class DichotomousKey(object):
	def __init__(self, name=None, author=None, year=None, steps=[]):
		self.name = name
		self.author = author
		self.year = year
		self.steps = steps

	def set_name(self):
		self.name = input("Dichotomous Key name: ")

	def set_year(self):
		self.year = input("Year of creation: ")

	def set_author(self):
		self.author = input("Author: ")

	def finalize(self):
		print("Dichotomous key information")
		print("Key name: %s" %(self.name))
		print("Year: %s" %(self.year))
		print("Author: %s" % (self.author))
		print("----------------------------")

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
				self.finalize()
				print("Your animal is: %s" %(self.steps[level].animal))
			else:
				self.execute(self.steps[level].get_list_index(self.steps[level].goto))
		elif choice == 'b':
			if self.steps[level+1].has_animal():
				self.finalize()
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
d_key.set_name()
d_key.set_year()
d_key.set_author()
d_key.load('six_legs_well_dev_wings')
d_key.execute(0)