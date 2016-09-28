#!/usr/bin/env python



strs = []
for n in range(int(raw_input())):
    strs.append(raw_input().strip())

queries = []
for q in range(int(raw_input())):
    queries.append(raw_input().strip())

for query in queries:
    print strs.count(query)    
