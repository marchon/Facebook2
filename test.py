import csv
import networkx as nx
from unidecode import unidecode
index=dict()
r = csv.reader(open('cleaned_index.csv','r'))
r.next()
for line in r:
    index[line[0]]=line[1]
	
Glist=list()
for f in range(1,16):
	file = open('train/train'+ str(f)+'.txt', 'r')
	data = file.readlines()
	dg = nx.MultiDiGraph()	
	for line in data:
		chars = [char for char in line.split(' | ') if len(char)]
		dg.add_edge(int(index[chars[0].strip()]),int(index[chars[1].strip()]),Cost=int(chars[2].strip()))
	file.close()
	print len(dg.edges())
	Glist.append(dg)

file = open('paths.txt', 'r')
data = file.readlines()
count=0
for line in data:
	chars = [char for char in line.split(' | ') if len(char)]
	path_to_test=list()
	for i in range(0,len(chars)):
		path_to_test.append(int(index[chars[i].strip()]))
	score=0
	for G in Glist:
		try:
			if path_to_test in [p for p in nx.all_shortest_paths(G,source=path_to_test[0],target=path_to_test[len(path_to_test)-1],weight='Cost')]:
				score=score+1
		except:
			pass
	print float(score/15)		
	count=count+1
	print count	
		
	
file.close()