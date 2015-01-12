#Represents the entire memory bank of the TB-3 (64 patterns in total)
class TB3Bank:
	BANK_SIZE = 64
	def __init__(self,patterns=None):
		if(patterns != None):
			self.patterns = patterns
		else:
			self.patterns = []
		
	def get_patterns(self):
		return self.patterns
		
	def get_pattern(self,index):
		return self.patterns[index]

	def add_pattern(self,pattern):
		self.patterns.append(pattern)
