#Represents a single pattern in the TB-3 bank
class TB3Pattern:

	#Dictionary keys used for parsing and accessing parameters
	KEY_PARAM_TRIPLET = "TRIPLET"
	KEY_PARAM_LAST_STEP = "LAST_STEP"
	KEY_PARAM_GATE_WIDTH = "GATE_WIDTH"
	KEY_PARAM_BANK = "BANK"
	KEY_PARAM_PATCH = "PATCH"
	KEY_STEP = "STEP"

	#New Pattern constructor, fill pattern with default parameters
	def __init__(self,steps,params):
	
		if(steps != None and params != None):
			self.steps = steps
			self.params = params
		else:
			self.steps = []
			self.params = {}
			
			self.params[TB3Pattern.KEY_PARAM_TRIPLET] = 0
			self.params[TB3Pattern.KEY_PARAM_LAST_STEP] = 15
			self.params[TB3Pattern.KEY_PARAM_GATE_WIDTH] = 67
			self.params[TB3Pattern.KEY_PARAM_BANK] = 0
			self.params[TB3Pattern.KEY_PARAM_PATCH] = -1
			
			for step in range(0,32):
				self.steps.append(TB3Step())

	def get_note(self,index):
		return notes[index]
	def get_param(self,key):
		return self.params[key]
	def get_steps(self):
		return self.steps
	def get_params(self):
		return self.params