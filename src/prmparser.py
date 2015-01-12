from tb3step import TB3Step
from tb3pattern import TB3Pattern

#Used to build TB3Pattern objects from Roland .PRM files
class PRMParser:
	def __init__(self,prm_data):
		self.prm_data = prm_data
		self.steps = []
		self.params = {}		
		
	def _inside_paren(self,line):
		start_paren = line.find("(")
		end_paren = line.find(")")
		
		if(not start_paren or not end_paren):
			print "Invalid line: %s" % line_note
			return ""
			
		start_paren += 1
		
		arg_str = line[start_paren:end_paren]
		
		return arg_str
		
	def _param_name(self,line):
		return line.split("(")[0]
		
	def _parse_param(self,line_arg):
		if not(line_arg.find("(") != -1 and line_arg.find(")") != -1 and line_arg.find(";") != -1):
			return
			
		param_args = self._inside_paren(line_arg)
		self.params[self._param_name(line_arg)] = int(param_args)
	
	def _parse_step(self,line_note):

		arg_str = self._inside_paren(line_note)
		if(arg_str == ""):
			return
		
		args = arg_str.split(",")
		
		if(len(args) != 4):
			print "Invalid number of note arguments(%s): %s" % (len(args),line_note)
		
		step = {}
		try:
			step[TB3Step.KEY_NOTE] = int(args[0])
			step[TB3Step.KEY_ACCENT] = bool(int(args[1]))
			step[TB3Step.KEY_CLEAR] = bool(int(args[2]))
			step[TB3Step.KEY_SLIDE] = bool(int(args[3]))
		except ValueError:
			print "ValueError triggered by line: %s" % line_note

		self.steps.append(TB3Step(step))
		
	def parse(self):
		prm_data = self.prm_data
		for line in prm_data.split("\n"):
			
			if(line[0:4].find(TB3Pattern.KEY_STEP) != -1):
				self._parse_step(line)
			elif(len(line) >= 1):
				self._parse_param(line)
		return self._get_pattern()	
		
	def _get_pattern(self):
		return TB3Pattern(self.steps,self.params)
		