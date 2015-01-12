import midi

class MIDIBuilder:

	SLIDE_TICK_LENGTH = 1
	TB3_CHANNEL = 2

	def __init__(self,pattern):
		self.pattern = pattern
		
	def _accent_to_velocity(self,accent):
		if(accent):
			return 127
		else:
			return 64
			
	def build(self):
		pattern = midi.Pattern()
		track = midi.Track()
		pattern.append(track)
		
		#Pulses per quarter
		ppq = pattern.resolution
		
		tb3_step_distance = ppq / 4
		
		first_note = True
		note_slide = False
		
		steps = self.pattern.get_steps()
		
		step_index = 0
		
		slide_offset = 0
		clear_flag = False
		clear_offset = 0
		
		for step in steps:
			
			
			if(first_note):
				track.append(midi.NoteOnEvent(tick=0,velocity=self._accent_to_velocity(step.get_accent()),pitch=step.get_note(),channel=MIDIBuilder.TB3_CHANNEL))
				first_note = False
				
			else:
				if(step.get_clear()):
					#End last note if there was one
					if(not steps[step_index-1].get_clear()):
						track.append(midi.NoteOffEvent(tick=tb3_step_distance - slide_offset + clear_offset,pitch=steps[step_index-1].get_note(),channel=MIDIBuilder.TB3_CHANNEL))
					else:
						clear_offset += tb3_step_distance
					step_index += 1
					clear_flag = True
					continue
					
				if(note_slide):
					#Start new note first
					track.append(midi.NoteOnEvent(tick=tb3_step_distance - slide_offset + clear_offset,velocity=self._accent_to_velocity(step.get_accent()),pitch=step.get_note(),channel=MIDIBuilder.TB3_CHANNEL))
					slide_offset = 0
					
					#End last note
					track.append(midi.NoteOffEvent(tick=MIDIBuilder.SLIDE_TICK_LENGTH,pitch=steps[step_index-1].get_note(),channel=MIDIBuilder.TB3_CHANNEL))
					slide_offset += MIDIBuilder.SLIDE_TICK_LENGTH
					
					clear_flag = False
				else:
					#End last note first
					if(not clear_flag):
						track.append(midi.NoteOffEvent(tick=tb3_step_distance - slide_offset + clear_offset,pitch=steps[step_index-1].get_note(),channel=MIDIBuilder.TB3_CHANNEL))
						slide_offset = 0

					#Start new note
					track.append(midi.NoteOnEvent(tick=0,velocity=self._accent_to_velocity(step.get_accent()),pitch=step.get_note(),channel=MIDIBuilder.TB3_CHANNEL))
					
					clear_flag = False
					
				#Reset clear offset since we had a note
				clear_offset = 0
				
			if(step.get_slide()):
				note_slide = True
			else:
				note_slide = False
			
			step_index += 1
			
		return pattern
		
		