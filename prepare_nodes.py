import csv
import math
import difflib
from unidecode import unidecode
import phonetics as ph
import re

def unique_list(l):
    ulist = []
    [ulist.append(x.upper()) for x in re.findall(r'\w+', l) if (x.upper() not in ulist) ]
    return ulist

k=0	
nodes=dict()

file = open('paths.txt', 'r')
data = file.readlines()
for line in data:
	chars = [char for char in line.split(' | ') if len(char)]
	for i in range(0,len(chars)):
		nodes[chars[i].strip()]=[k+i]
		nodes[chars[i].strip()].append(ph.metaphone(str(unique_list(unidecode((chars[i]).strip())))))
	k=k+len(chars)
	print k
file.close()

for f in range(1,16):
	file = open('train/train'+ str(f)+'.txt', 'r')
	data = file.readlines()
		
	for line in data:
		chars = [char for char in line.split(' | ') if len(char)]
		nodes[chars[0].strip()]=[k]
		nodes[chars[0].strip()].append(ph.metaphone(str(unique_list(unidecode((chars[0]).strip())))))
		nodes[chars[1].strip()]=[k+1]
		nodes[chars[1].strip()].append(ph.metaphone(str(unique_list(unidecode((chars[1]).strip())))))
		k=k+2
		print k
		
	file.close()


print len(nodes)

file = open('nodes.csv','wb')
w = csv.writer(file)
w.writerow(['source_node','ASID'])
for node in sorted(nodes):
	w.writerow([node, ''.join(nodes[node][1:2])])
file.close()


