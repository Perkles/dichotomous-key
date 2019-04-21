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
			self.execute(self.steps[level].get_list_index(self.steps[level].goto))
		elif choice == 'b':
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
		if int(goto) == 2:
			return (int(goto) * 2) - 1
		else:
			return (int(goto) * 2) - 2

d_key = DichotomousKey()
d_key.load('six_legs_well_dev_wings')
d_key.execute(0)