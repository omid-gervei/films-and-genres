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
    final.extend(q[1:])
    #a = ['a','f','d','a']
    #a.count('a')
d = {}
for i in final:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
   
res = {val[0] : val[1] for val in sorted(d.items(), key = lambda x: (-x[1], x[0]))}    

for k,v in res.items():
    print(k,':',v)

#print(res)
    