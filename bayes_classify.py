#!/usr/bin/python

import common
import json
import numpy
import sys
import re
import math
import glob
import os

# input: songs (possibly to classify)
# output: categories, category_prediction_percentage
def map(line):
	line_split=re.split("\t",line)
	track_id=line_split[0]
	track_data=json.loads(line_split[1])
	artist_id=track_data["artist_id"]
	if(not artist_dict.has_key(artist_id)):
		# find the actual term we're looking for
		artist_terms=track_data["artist_terms"]
		if len(artist_terms)>0:
			term_frequencies=track_data["artist_terms_freq"]
			top_term=0
			for i in range(len(artist_terms)):
				if(term_frequencies[i]>term_frequencies[top_term]):
					top_term=i
			actual_term=artist_terms[i]
			# calculate the probabilities for each term, find top
			top_probability_term=actual_term # initialize top term
			top_probability=0
			for classifier_term,classifier_data in classifier.items():
				probabilities=[]
				count=classifier_data[0]
				means=classifier_data[1]
				variances=classifier_data[2]
				for data_label in means.keys():
					track_value=track_data[data_label]
					mean=means[data_label]
					variance=variances[data_label]
					# check to see if we're a list; if so, iterate over that list
					if(getattr(mean,'__iter__',False)):
						for i in range (0,len(mean)):
							if variance[i]>0:
								probability=(count/1000000)*(1/math.sqrt(variance[i]*2*math.pi))*math.exp(-(track_value[i]-mean[i])**2/(2*variance[i]))
								probabilities.append(probability)
					else:	
						if variance>0:
							probability=(count/1000000)*(1/math.sqrt(variance*2*math.pi))*math.exp(-(track_value-mean)**2/(2*variance))
							probabilities.append(probability)
#							print str(track_value)+" "+str(mean)+" "+str(variance)+" "+str(probability)
				term_probability=numpy.prod(numpy.array(probabilities))
				print classifier_term+" "+str(term_probability)
				if term_probability>top_probability:
					top_probability=term_probability
					top_probability_term=classifier_term
			yield("1",actual_term+","+top_probability_term+","+str(top_probability))
		
# output: actual category, correct prediction %, wrong prediction %
def reduce(word, counts):
	false_positives={}
	false_negatives={}
	correct={}
	for key in classifier.keys():
		correct[key]=0
		false_positives[key]=0
		false_negatives[key]=0
	for count in counts:
		count_split=re.split(",",count)
		actual_term=count_split[0]
		top_probability=count_split[1]
		print actual_term+" "+top_probability
		# we only want to do this if it's one of the categories we classify
		if actual_term in classifier.keys():
			print "****MATCH****"
			# and classify into correct/incorrect buckets
			if(top_probability==actual_term):
				correct[actual_term]+=1
			else:
				false_positives[top_probability]+=1
				false_negatives[actual_term]+=1
	for term in classifier.keys():
		if((correct[term]+false_negatives[term])>0):
			correct_percent=correct[term]/(correct[term]+false_negatives[term])
		if((correct[term]+false_negatives[term])>0):
			false_negative_percent=false_negatives[term]/(correct[term]+false_negatives[term])
		if((correct[term]+false_positives[term])>0):
			false_positive_percent=false_positives[term]/(correct[term]+false_positives[term])
		yield(term,str(correct_percent)+"\t"+str(false_negative_percent)+"\t"+str(false_positive_percent))
		

if __name__ == "__main__":
	# create dictionary of test artists
	global artist_dict
	artist_dict={}
	f = open("artists_train.txt",'r')
	for artist in f:
		artist_dict[artist.rstrip()]=1
	f.close()
	global classifier
	classifier={}
	path = 'build_bayes/'
	for infile in glob.glob( os.path.join(path, 'part*') ):
		f = open(infile,'r')
		for classifier_line in f:
			classifier_line_split=re.split("\t",classifier_line.rstrip())
			classifier[classifier_line_split[0]]=json.loads(classifier_line_split[1])
		f.close()
	common.main(map, reduce)
