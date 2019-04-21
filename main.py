import csv

my_key = []


class DichotomousKey(object):
	def __init__(self, level=None, argument=None, instruction=None, animal=None, pointer=1):
		self.level = level
		self.argument = argument
		self.instruction = instruction
		self.animal = animal
		self.pointer = pointer

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
			level, argument, instruction, animal = row
			return my_key.append(DichotomousKey(level, argument, instruction, animal))
		else:
			level, argument, instruction = row
			return my_key.append(DichotomousKey(level, argument, instruction))

	'''

	def key(self, key):
		for item in key:
			if (item.level == str(self.pointer)) or (item.level == str(self.pointer)):
				print(item.level + ' : ' + item.argument)
		decision = self.decision(input())

	def decision(self, decision):
		if decision == 'a':
			self.pointer = int(my_key[self.pointer].instruction)
		elif decision == 'b':
			self.pointer = int(my_key[self.pointer].instruction)
		self.pointer += 1
		self.key(my_key)

	'''
d_key = DichotomousKey()
d_key.load('six_legs_well_dev_wings')
#d_key.key(my_key)

# 17 levels

# 2a	-	1a / DIPTERA

# 2b	-	1a / EPHEMEROPTERA

# 4a	-	3a	-	3a	-	1b / LEPIDOPTERA

# 14a	-	3b	-	3b	-	1b / HETEROPTERA

# 15a	-	14b	-	14b	-	3b	-	3b	-	1b / COLEOPTERA

# 6a	-	5a	-	5a	-	4b	-	4b	-	3a	-	3a	-	1b / TRICHOPTERA

# 16b	-	15b	-	15b	-	14b	-	14b	-	3b	-	3b	-	14b / BLATTARIA

# 10a	-	9a	-	9a -	5b	-	5b	-	4b	-	4b	-	3a	-	3a	-	1b / ODONATA 

# 7a	-	6b	-	6b	-	5a	-	5a	-	4b	-	4b	-	3a	-	3a	-	1b / HOMOPTERA

# 12b	-	9b	-	9b	-	5b	-	5b	-	4b	-	4b	-	3a	-	3a	-	1b / HYMENOPTERA

# 17a	-	16a	-	16a	-	15b	-	15b	-	14b	-	14b	-	3b	-	3b	-	1b / MANTODEA

# 17b	-	16a	-	16a	-	15b	-	15b	-	14b	-	14b	-	3b	-	3b	-	1b / ORTHOPTERA

# 8a	-	7b	-	7b	-	6b	-	6b	-	5a	-	5a	-	4b	-	4b	-	3a	-	3a	-	1b / NEUROPTERA

# 8b	-	7b	-	7b	-	6b	-	6b	-	5a	-	5a	-	4b	-	4b	-	3a	-	3a	-	1b / PSOCOPTERA

# 11a	-	10b	-	10b	-	9a	-	9a	-	5b	-	5b	-	4b	-	4b	-	3a	-	3a	-	1b / ISOPTERA

# 11b	-	10b	-	10b	-	9a	-	9a	-	5b	-	5b	-	4b	-	4b	-	3a	-	3a	-	1b / MECOPTERA

# 13a	-	12a	-	12a	-	9b	-	9b	-	5b	-	5b	-	4b	-	4b	-	3a	-	3a	-	1b / EPHEMEROPTERA
