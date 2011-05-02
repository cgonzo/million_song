
import hdf5_getters

def classify(h5):
	output_array=[]
	# duration
	duration=hdf5_getters.get_duration(h5)
	output_array.append(duration)	### ADDED VALUE TO ARRAY
	# number of bars
	bars=hdf5_getters.get_bars_start(h5)
	num_bars=len(bars)
	output_array.append(num_bars)	### ADDED VALUE TO ARRAY
	# mean and variance in bar length
	bar_length=[]
	for i in range(1,len(bars)):
		bar_length.append(bars[i]-bars[i-1])
	mean_bar_length=num_bars/duration
	variance_bar_length=0
	for bar_length_element in bar_length:
		variance_bar_length+=(bar_length_element-mean_bar_length)**2
	if len(bar_length)>0:
		variance_bar_length/=len(bar_length)
	else:
		variance_bar_length=0
	output_array.append(variance_bar_length)	### ADDED VALUE TO ARRAY
	# number of beats
	beats=hdf5_getters.get_beats_start(h5)
	num_beats=len(beats)
	output_array.append(num_beats)	### ADDED VALUE TO ARRAY
	# mean and variance in beats length
	beats_length=[]
	for i in range(1,len(beats)):
		beats_length.append(beats[i]-beats[i-1])
	mean_beats_length=num_beats/duration
	variance_beats_length=0
	for beats_length_element in beats_length:
		variance_beats_length+=(beats_length_element-mean_beats_length)**2
	if len(beats_length)>0:
		variance_beats_length/=len(beats_length)
	else:
		variance_beats_length=0
	output_array.append(variance_beats_length)	### ADDED VALUE TO ARRAY
	# danceability
	danceability=hdf5_getters.get_danceability(h5)
	output_array.append(danceability)	### ADDED VALUE TO ARRAY
	# end of fade in
	end_of_fade_in=hdf5_getters.get_end_of_fade_in(h5)
	output_array.append(end_of_fade_in)	### ADDED VALUE TO ARRAY
	# energy
	energy=hdf5_getters.get_energy(h5)
	output_array.append(energy)	### ADDED VALUE TO ARRAY
	# key
	key=hdf5_getters.get_key(h5)
	output_array.append(key)	### ADDED VALUE TO ARRAY
	# loudness
	loudness=hdf5_getters.get_loudness(h5)
	output_array.append(loudness)	### ADDED VALUE TO ARRAY
	# mode
	mode=hdf5_getters.get_mode(h5)
	output_array.append(mode)	### ADDED VALUE TO ARRAY
	# number sections
	sections=hdf5_getters.get_sections_start(h5)
	num_sections=len(sections)
	output_array.append(num_sections)	### ADDED VALUE TO ARRAY
	# mean and variance in sections length
	sections_length=[]
	for i in range(1,len(sections)):
		sections_length.append(sections[i]-sections[i-1])
	mean_sections_length=num_sections/duration
	variance_sections_length=0
	for sections_length_element in sections_length:
		variance_sections_length+=(sections_length_element-mean_sections_length)**2
	if len(sections_length)>0:
		variance_sections_length/=len(sections_length)
	else:
		variance_sections_length=0
	output_array.append(variance_sections_length)	### ADDED VALUE TO ARRAY
	# number segments
	segments=hdf5_getters.get_segments_start(h5)
	num_segments=len(segments)
	output_array.append(num_segments)	### ADDED VALUE TO ARRAY
	# mean and variance in segments length
	segments_length=[]
	for i in range(1,len(segments)):
		segments_length.append(segments[i]-segments[i-1])
	mean_segments_length=num_segments/duration
	variance_segments_length=0
	for segments_length_element in segments_length:
		variance_segments_length+=(segments_length_element-mean_segments_length)**2
	if len(segments_length)>0:
		variance_segments_length/=len(segments_length)
	else:
		variance_segments_length=0
	output_array.append(variance_segments_length)	### ADDED VALUE TO ARRAY
	# segment loudness max
	segment_loudness_max_array=hdf5_getters.get_segments_loudness_max(h5)
	segment_loudness_max_time_array=hdf5_getters.get_segments_loudness_max_time(h5)
	segment_loudness_max_index=0
	for i in range(len(segment_loudness_max_array)):
		if segment_loudness_max_array[i]>segment_loudness_max_array[segment_loudness_max_index]:
			segment_loudness_max_index=i
	segment_loudness_max=segment_loudness_max_array[segment_loudness_max_index]
	segment_loudness_max_time=segment_loudness_max_time_array[segment_loudness_max_index]
	output_array.append(segment_loudness_max)	### ADDED VALUE TO ARRAY
	output_array.append(segment_loudness_max_time)	### ADDED VALUE TO ARRAY
			
	# segment loudness mean (start)
	segment_loudness_array=hdf5_getters.get_segments_loudness_start(h5)
	weighted_segment_loudness_array=[]
	for i in range(len(segment_loudness_array)-1):
		weighted_segment_loudness_array.append(segment_loudness_array[i]*segments_length[i])
	segment_loudness_mean=sum(weighted_segment_loudness_array)/duration
	output_array.append(segment_loudness_mean)	### ADDED VALUE TO ARRAY
	# segment loudness variance (start)
	weighted_segment_loudness_variance_array=[]
	for i in range(len(segment_loudness_array)-1):
		weighted_segment_loudness_array.append((segment_loudness_array[i]-segment_loudness_mean)**2*segments_length[i])
	segment_loudness_variance=sum(weighted_segment_loudness_array)/duration
	output_array.append(segment_loudness_variance)	### ADDED VALUE TO ARRAY
	# segment pitches
	segment_pitches_array=hdf5_getters.get_segments_pitches(h5)
	weighted_segment_pitches_array=[]
	for i in range(len(segment_pitches_array)-1):
		weighted_segment_pitches_array.append(segment_pitches_array[i]*segments_length[i])
	segment_pitches_mean=sum(weighted_segment_pitches_array)/duration
	for element in segment_pitches_mean:
		output_array.append(element)	### ADDED VALUE TO ARRAY
	# segment pitches variance (start)
	weighted_segment_pitches_variance_array=[]
	for i in range(len(segment_pitches_array)-1):
		weighted_segment_pitches_array.append((segment_pitches_array[i]-segment_pitches_mean)**2*segments_length[i])
	segment_pitches_variance=sum(weighted_segment_pitches_array)/duration
	for element in segment_pitches_variance:
		output_array.append(element)	### ADDED VALUE TO ARRAY
	# segment timbres
	segment_timbres_array=hdf5_getters.get_segments_timbre(h5)
	weighted_segment_timbres_array=[]
	for i in range(len(segment_timbres_array)-1):
		weighted_segment_timbres_array.append(segment_timbres_array[i]*segments_length[i])
	segment_timbres_mean=sum(weighted_segment_timbres_array)/duration
	for element in segment_timbres_mean:
		output_array.append(element)	### ADDED VALUE TO ARRAY
	# segment timbres variance (start)
	weighted_segment_timbres_variance_array=[]
	for i in range(len(segment_timbres_array)-1):
		weighted_segment_timbres_array.append((segment_timbres_array[i]-segment_timbres_mean)**2*segments_length[i])
	segment_timbres_variance=sum(weighted_segment_timbres_array)/duration
	for element in segment_timbres_variance:
		output_array.append(element)	### ADDED VALUE TO ARRAY
	# hotttnesss
	hottness=hdf5_getters.get_song_hotttnesss(h5,0)
	output_array.append(hottness)	### ADDED VALUE TO ARRAY
	# duration-start of fade out
	start_of_fade_out=hdf5_getters.get_start_of_fade_out(h5)
	fade_out=duration-start_of_fade_out
	output_array.append(fade_out)	### ADDED VALUE TO ARRAY
	# tatums
	tatums=hdf5_getters.get_tatums_start(h5)
	num_tatums=len(tatums)
	output_array.append(num_tatums)	### ADDED VALUE TO ARRAY
	# mean and variance in tatums length
	tatums_length=[]
	for i in range(1,len(tatums)):
		tatums_length.append(tatums[i]-tatums[i-1])
	mean_tatums_length=num_tatums/duration
	variance_tatums_length=0
	for tatums_length_element in tatums_length:
		variance_tatums_length+=(tatums_length_element-mean_tatums_length)**2
	if len(tatums_length)>0:
		variance_tatums_length/=len(tatums_length)
	else:
		variance_tatums_length=0
	output_array.append(variance_tatums_length)	### ADDED VALUE TO ARRAY
	# tempo
	tempo=hdf5_getters.get_tempo(h5)
	output_array.append(tempo)	### ADDED VALUE TO ARRAY
	# time signature
	time_signature=hdf5_getters.get_time_signature(h5)
	output_array.append(time_signature)	### ADDED VALUE TO ARRAY
	# year
	year=hdf5_getters.get_year(h5)
	output_array.append(year)	### ADDED VALUE TO ARRAY

	return output_array
