import csv
import math
import difflib
import re


k=0	
nodes=dict()
r = csv.reader(open('nodes.csv','r'))
r.next()
nodes = dict()
for line in r:
	if line[1]=='':
		nodes[line[0]]=k
	else:
		nodes[line[1]]=k
	k=k+1

print len(nodes)
count=0
i=0
temp_list=sorted(nodes.keys())
while i<len(temp_list)-1:

	for j in range(i+1,len(temp_list)+1):
		score=difflib.SequenceMatcher(None, temp_list[i], temp_list[j]).ratio()
		if (score > 0.525) &  (not temp_list[j].isdigit()):
			print temp_list[i]
			print temp_list[j]
			nodes[temp_list[j]]=nodes[temp_list[i]]
			print nodes[temp_list[j]]
			count=count+1
		else:
			i=j
			break
	
	print count

file = open('fastindex.csv','wb')
w = csv.writer(file)
w.writerow(['source_node','ASID'])
for node in sorted(nodes):
	w.writerow([node, str(nodes[node])])
file.close()


