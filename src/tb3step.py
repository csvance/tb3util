import midi

#Represents a single step in the TB-3 sequencer
class TB3Step:

	KEY_NOTE = "NOTE"
	KEY_ACCENT = "ACCENT"
	KEY_CLEAR = "CLEAR"
	KEY_SLIDE = "SLIDE"

	#New step constructor, fill step with default parameters
	def __init__(self,step_dict=None):
		if(step_dict == None):
			self._init(midi.C_3,False,True,False)
		else:
			self._init(step_dict[TB3Step.KEY_NOTE],step_dict[TB3Step.KEY_ACCENT],step_dict[TB3Step.KEY_CLEAR],step_dict[TB3Step.KEY_SLIDE])
			
	def __repr__(self):
		return "TB3Step(note=%s,accent=%s,clear=%s,slide=%s)" % (self.note,self.accent,self.clear,self.slide)

	def _init(self,note,accent,clear,slide):
		self.note = note
		self.accent = accent
		self.clear = clear
		self.slide = slide
	
	def get_note(self):
		return self.note
	def get_accent(self):
		return self.accent
	def get_clear(self):
		return self.clear
	def get_slide(self):
		return self.slide