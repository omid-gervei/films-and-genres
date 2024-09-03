# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:50:16 2024

@author: omidg
"""

final = []
a = int(input())
for i in range(0,a):
    file = input()
    q = file.split(' ')
    final.extend(q[1:]) # the first input with index 0 is the name of person
    
# Now in final we have a list containing the genres that the input people likes
# we create a dictionary for calculating the number of each genres available in the list 
    
d = {}
for i in final:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
#Given a dictionary, sort according to descended values, if similar values, then by keys lexicographically.   
res = {val[0] : val[1] for val in sorted(d.items(), key = lambda x: (-x[1], x[0]))}    

for k,v in res.items():
    print(k,':',v)

#print(res)
    