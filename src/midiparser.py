import midi

from tb3step import TB3Step
from tb3pattern import TB3Pattern

class MIDIParser:
	def __init__(self,midi_path):
		self.midi_path = midi_path
		
	def parse(self,track_index=0):
		pattern = midi.read_midifile(self.midi_path)
		
		track = pattern[track_index] 
		
		#Pulses per quarter
		ppq = pattern.resolution
		
		tb3_step_distance = ppq / 4

		#Count how many notes are current playing, used to calculate sliding
		noteon = 0
		
		slide = False
		accent = False

		last_note_on = 0
		current_time = 0
		
		step_count = 0
		
		steps = []
		
		for event in track:
		
			current_time += event.tick
		
			#We are only interested in NoteOn / NoteOff events
			if(isinstance(event,midi.NoteOnEvent)):
			
			
				#Check for skipped areas with no notes
				while(current_time >= last_note_on + tb3_step_distance*1.5):
					steps.append(TB3Step())
					step_count += 1
					last_note_on += tb3_step_distance

				if(noteon > 0):
					slide = True
				else:
					slide = False
				
				#Based on MIDI recorded from the TB-3 accented notes should work with 127 velocity and unaccented should work with 64
				if(event.get_velocity() <= 64):
					accent = False
				elif(event.get_velocity() <= 127):
					print "wat"
					accent = True
				
				step = {}
				step[TB3Step.KEY_NOTE] = event.get_pitch()
				step[TB3Step.KEY_ACCENT] = accent
				step[TB3Step.KEY_CLEAR] = False
				step[TB3Step.KEY_SLIDE] = slide

				steps.append(TB3Step(step))
				step_count += 1
				
				last_note_on = current_time
				noteon += 1
				if(noteon > 2):
					print "Warning: more than two noteon event active! Expect wierd behavior"
				
			elif(isinstance(event,midi.NoteOffEvent)):
				
				noteon -= 1
				pass
				
		params = {}
		params[TB3Pattern.KEY_PARAM_TRIPLET] = 0
		params[TB3Pattern.KEY_PARAM_LAST_STEP] = step_count-1
		params[TB3Pattern.KEY_PARAM_GATE_WIDTH] = 67
		params[TB3Pattern.KEY_PARAM_BANK] = 0
		params[TB3Pattern.KEY_PARAM_PATCH] = -1
		return TB3Pattern(steps,params)
