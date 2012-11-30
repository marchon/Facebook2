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
print len(Glist)

	