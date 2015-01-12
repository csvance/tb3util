from tb3step import TB3Step
from tb3pattern import TB3Pattern

#Used to construct Roland .PRM files from a TB3Pattern object
class PRMBuilder:

	def __init__(self,pattern): 
		self.pattern = pattern
		
	def _make_param_line(self,key):
		return "%s(%s);\n" % (key,self.pattern.get_param(key))

	def _make_step_line(self,step_count,step):
		return "%s%s(%s,%s,%s,%s);\n" % (TB3Pattern.KEY_STEP,step_count,step.get_note(),int(step.get_accent()),int(step.get_clear()),int(step.get_slide()))

	def build(self):
		prm_string = ""
		prm_string += self._make_param_line(TB3Pattern.KEY_PARAM_TRIPLET)
		prm_string += self._make_param_line(TB3Pattern.KEY_PARAM_LAST_STEP)
		prm_string += self._make_param_line(TB3Pattern.KEY_PARAM_GATE_WIDTH)
		
		step_count = 1
		for step in self.pattern.get_steps():
			prm_string += self._make_step_line(step_count,step)
			step_count += 1
			
		prm_string += self._make_param_line(TB3Pattern.KEY_PARAM_BANK)
		prm_string += self._make_param_line(TB3Pattern.KEY_PARAM_PATCH)
		
		return prm_string