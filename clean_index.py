import csv
import math
import difflib
import re

global freq_words
freq_words=[]
file = open('freq_words.txt', 'r')
data = file.readlines()
[freq_words.append(line.rstrip('\n')) for line in data]

def unique_list(l):
    ulist = []
    [ulist.append(x.upper()) for x in re.findall(r'\w+', l) if (x.upper() not in ulist) & (x.upper() not in freq_words)]
    return ulist

k=0	
index=dict()
r = csv.reader(open('index.csv','r'))
r.next()
for line in r:
    index[line[0]]=line[1]
	
print len(index)
count=0
i=0
temp_list=sorted(index.keys())
while i<len(temp_list)-1:
	count=count+1
	for j in range(i+1,len(temp_list)+1):
		score=difflib.SequenceMatcher(None, unique_list(temp_list[i]), unique_list(temp_list[j])).ratio()
		if (score > 0.7) &  (not temp_list[j].isdigit()) & (index[temp_list[j]]!=index[temp_list[i]]):
			print temp_list[i]
			print temp_list[j]
			index[temp_list[j]]=index[temp_list[i]]
			print index[temp_list[j]]
		else:
			i=j
			break
	
	print i

print count
file = open('cleaned_index.csv','wb')
w = csv.writer(file)
w.writerow(['source_node','ASID'])
for node in sorted(index):
	w.writerow([node, index[node]])
file.close()


