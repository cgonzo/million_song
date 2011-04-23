#!/usr/bin/python

import common
import re
import json

# mapper will output pagerank number of links and name of linker
# input: page [pagerank [list of links]]
# output: link [linker pagerank, linker] 
# will also output the original input
def map(line):
	# split into key,value
	line_split=re.split('\t',line)
	if len(line_split)==2:	# this should always be true
		linker_name=line_split[0]
		link_data=json.loads(line_split[1])
		pagerank=link_data[0]
		link_list=link_data[1]
		if link_list:	# to handle a page that doesn't link to anything
			pagerank=pagerank/len(link_list)
		for link in link_list:
			link=re.sub('\t',' ',link)
			output_data=[pagerank,linker_name]
  			yield(link,json.dumps(output_data))
  		link_data[0]='old'
  		yield(linker_name,json.dumps(link_data))

# reducer gathers all of these guys up and finds pagerank
# input: link [partial pagerank, linker] 
# output: page [pagerank [list of links]]
def reduce(word, counts):
	d=0.85
	pagerank=0
	list_of_links=[]
	for linker_json in counts:
		try:
			linker_list=json.loads(linker_json)
		except:
			raise NameError("Error with line"+linker_json)
		pagerank_data=linker_list[0]
		if pagerank_data == 'old':
			list_of_links=linker_list[1]
		else:
			pagerank+=pagerank_data
	pagerank=1-d+d*pagerank
	data_to_output=[pagerank, list_of_links]
	yield(word,json.dumps(data_to_output))
	#yield(word,str(pagerank_data))

if __name__ == "__main__":
  common.main(map, reduce)
