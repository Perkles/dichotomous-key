# class dichotomous_key(object):
# 	def __init__(self, level, argument_a, argument_b ):
# 		self.level = level
# 		self.a = {str(self.level) + 'a' : argument_a}
# 		self.b = {str(self.level) + 'b' : argument_b}

import csv

class dichotomous_key(object):
	def __init__(self, index = None, argument = None, instruction = None, animal = None, level = None, display = []):
		self.index = index
		self.argument = argument
		self.instruction = instruction
		self.animal = animal
		self.level = level
		self.display = []

	def load(self, file_name):
		with open(file_name + '.txt') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					self.add_to_display(row)
					line_count += 1
				else:
					self.add_to_display(row)
					line_count += 1

	def execute(self):

		level = 1
		while (level != (len(self.display))):
			print('got')
			# shesaid = list(filter(lambda x: x == "1", self.display))
			shesaid = map(self.index_match(self.display, level), self.display)
			print(shesaid)
			print('it')
			print(level, ' - ' , self.display[level], '\n')
			choice = int(input("digite algo: "))
			level += 1


	def getChoices(self):
		return self.display

	def add_to_display(self, row):
		if (len(row) == 4):
			self.display.append([row[0],row[1],row[2],row[3]])
		else:
			self.display.append([row[0],row[1],row[2]])

	def index_match(self, row, index):
		print("sdjagdjagdadas")
		print(row[index][0] == "1b")

		print(str(index))
		if (row[index][0] == str(index) + "a") or (row[index][0] == str(index) + "b"):
			return row
		else:
			return False


d_key = dichotomous_key()
d_key.load('six_legs_well_dev_wings')
# d_key.getChoices()
d_key.execute()

# d = dichotomous_key(1, 'One pair of wings go to 2' , 'Hind wings reduced to tiny knobs (halteres), tip of abdomen without 2-3 thread-like tails')
# d.a = dichotomous_key(2, 'asdasdsa' , 'asdasd')
# print(d)
# print(d.a.a)


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