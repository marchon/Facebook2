import csv

r = csv.reader(open('fastindex.csv','r'))
r.next()
fastindex = dict()
for line in r:
    fastindex[line[0]]=line[1]

r = csv.reader(open('nodes.csv','r'))
r.next()
nodes = dict()
for line in r:
	if line[1]=='':
		nodes[line[0]]=fastindex[line[0]]
	else:
		nodes[line[0]]=fastindex[line[1]]
	
file = open('index.csv','wb')
w = csv.writer(file)
w.writerow(['source_node','ASID'])
for node in sorted(nodes):
	w.writerow([node, str(nodes[node])])
file.close()