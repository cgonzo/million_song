
import hdf5_getters
import numpy

def classify(h5):
	output_array={}
	# duration
	duration=hdf5_getters.get_duration(h5)
	output_array["duration"]=duration	### ADDED VALUE TO ARRAY
	# number of bars
	bars=hdf5_getters.get_bars_start(h5)
	num_bars=len(bars)
	output_array["num_bars"]=num_bars	### ADDED VALUE TO ARRAY
	# mean and variance in bar length
	bar_length=numpy.ediff1d(bars)
	variance_bar_length=numpy.var(bar_length)
	output_array["variance_bar_length"]=variance_bar_length	### ADDED VALUE TO ARRAY
	# number of beats
	beats=hdf5_getters.get_beats_start(h5)
	num_beats=len(beats)
	output_array["num_beats"]=num_beats	### ADDED VALUE TO ARRAY
	# mean and variance in beats length
	beats_length=numpy.ediff1d(beats)
	variance_beats_length=numpy.var(bar_length)
	output_array["variance_beats_length"]=variance_beats_length	### ADDED VALUE TO ARRAY
	# danceability
	danceability=hdf5_getters.get_danceability(h5)
	output_array["danceability"]=danceability	### ADDED VALUE TO ARRAY
	# end of fade in
	end_of_fade_in=hdf5_getters.get_end_of_fade_in(h5)
	output_array["end_of_fade_in"]=end_of_fade_in	### ADDED VALUE TO ARRAY
	# energy
	energy=hdf5_getters.get_energy(h5)
	output_array["energy"]=energy	### ADDED VALUE TO ARRAY
	# key
	key=hdf5_getters.get_key(h5)
	output_array["key"]=int(key)	### ADDED VALUE TO ARRAY
	# loudness
	loudness=hdf5_getters.get_loudness(h5)
	output_array["loudness"]=loudness	### ADDED VALUE TO ARRAY
	# mode
	mode=hdf5_getters.get_mode(h5)
	output_array["mode"]=int(mode)	### ADDED VALUE TO ARRAY
	# number sections
	sections=hdf5_getters.get_sections_start(h5)
	num_sections=len(sections)
	output_array["num_sections"]=num_sections	### ADDED VALUE TO ARRAY
	# mean and variance in sections length
	sections_length=numpy.ediff1d(sections)
	variance_sections_length=numpy.var(sections)
	output_array["variance_sections_length"]=variance_sections_length	### ADDED VALUE TO ARRAY
	# number segments
	segments=hdf5_getters.get_segments_start(h5)
	num_segments=len(segments)
	output_array["num_segments"]=num_segments	### ADDED VALUE TO ARRAY
	# mean and variance in segments length
	segments_length=numpy.ediff1d(segments)
	variance_segments_length=numpy.var(segments)
	output_array["variance_segments_length"]=variance_segments_length	### ADDED VALUE TO ARRAY
	# segment loudness max
	segment_loudness_max_array=hdf5_getters.get_segments_loudness_max(h5)
	segment_loudness_max_time_array=hdf5_getters.get_segments_loudness_max_time(h5)
	segment_loudness_max_index=0
	for i in range(len(segment_loudness_max_array)):
		if segment_loudness_max_array[i]>segment_loudness_max_array[segment_loudness_max_index]:
			segment_loudness_max_index=i
	segment_loudness_max=segment_loudness_max_array[segment_loudness_max_index]
	segment_loudness_max_time=segment_loudness_max_time_array[segment_loudness_max_index]
	output_array["segment_loudness_max"]=segment_loudness_max	### ADDED VALUE TO ARRAY
	output_array["segment_loudness_time"]=segment_loudness_max_time	### ADDED VALUE TO ARRAY
			
	# POSSIBLE TODO: use average function instead and weight by segment length
	# segment loudness mean (start)
	segment_loudness_array=hdf5_getters.get_segments_loudness_start(h5)
	segment_loudness_mean=numpy.mean(segment_loudness_array)
	output_array["segment_loudness_mean"]=segment_loudness_mean	### ADDED VALUE TO ARRAY
	# segment loudness variance (start)
	segment_loudness_variance=numpy.var(segment_loudness_array)
	output_array["segment_loudness_variance"]=segment_loudness_variance	### ADDED VALUE TO ARRAY
	# segment pitches
	segment_pitches_array=hdf5_getters.get_segments_pitches(h5)
	segment_pitches_mean=numpy.mean(segment_pitches_array,axis=0).tolist()
	output_array["segment_pitches_mean"]=segment_pitches_mean
	# segment pitches variance (start)
	segment_pitches_variance=numpy.var(segment_pitches_array,axis=0).tolist()
	output_array["segment_pitches_variance"]=segment_pitches_variance
	# segment timbres
	segment_timbres_array=hdf5_getters.get_segments_timbre(h5)
	segment_timbres_mean=numpy.mean(segment_timbres_array,axis=0).tolist()
	output_array["segment_timbres_mean"]=segment_timbres_mean
	# segment timbres variance (start)
	segment_timbres_variance=numpy.var(segment_timbres_array,axis=0).tolist()
	output_array["segment_timbres_variance"]=segment_timbres_variance
	# hotttnesss
	hottness=hdf5_getters.get_song_hotttnesss(h5,0)
	output_array["hottness"]=hottness	### ADDED VALUE TO ARRAY
	# duration-start of fade out
	start_of_fade_out=hdf5_getters.get_start_of_fade_out(h5)
	fade_out=duration-start_of_fade_out
	output_array["fade_out"]=fade_out	### ADDED VALUE TO ARRAY
	# tatums
	tatums=hdf5_getters.get_tatums_start(h5)
	num_tatums=len(tatums)
	output_array["num_tatums"]=num_tatums	### ADDED VALUE TO ARRAY
	# mean and variance in tatums length
	tatums_length=numpy.ediff1d(tatums)
	variance_tatums_length=numpy.var(tatums_length)
	output_array["variance_tatums_length"]=variance_tatums_length	### ADDED VALUE TO ARRAY
	# tempo
	tempo=hdf5_getters.get_tempo(h5)
	output_array["tempo"]=tempo	### ADDED VALUE TO ARRAY
	# time signature
	time_signature=hdf5_getters.get_time_signature(h5)
	output_array["time_signature"]=int(time_signature)	### ADDED VALUE TO ARRAY
	# year
	year=hdf5_getters.get_year(h5)
	output_array["year"]=int(year)	### ADDED VALUE TO ARRAY
	# artist terms
	artist_terms=hdf5_getters.get_artist_terms(h5,0)
	output_array["artist_terms"]=artist_terms.tolist()
	artist_terms_freq=hdf5_getters.get_artist_terms_freq(h5,0)
	output_array["artist_terms_freq"]=artist_terms_freq.tolist()
	artist_name=hdf5_getters.get_artist_name(h5,0)
	output_array["artist_name"]=artist_name

	return output_array
