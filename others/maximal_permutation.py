
import itertools
import time

def permutations(n):
    return itertools.permutations(range(1, n+1))

def distance(p):
      return min([abs(p1 - p2) for p1, p2 in itertools.izip(p, p[1:])])

def get_maximal_distance(n):
    maximal_distances = []
    current_max_distance = -1
    distance_map = {(item): abs(item[0] - item[1]) for item in itertools.permutations(range(1, n+1), 2)}
    s = time.time()
    print len(list(permutations(n)))
    #abc = [ distance_map[item] for p in permutations(n) for item in itertools.izip(p, p[1:])]
    print time.time() - s
    #print len(abc)
    #print abc
    print time.time() - s
    return []
    for p in permutations(n):
        continue
        distance_list = [abs(p1 - p2) for p1, p2 in itertools.izip(p, p[1:])]
        md = min(distance_list)
        if current_max_distance == md:
            maximal_distances.append(p)
        elif current_max_distance < md:
            current_max_distance = md
            maximal_distances = [p]
    print time.time() - s
    #print len(maximal_distances)
    #print maximal_distances
    return maximal_distances

def get_maximal_distance2(n):
    maximal_distances = []
    current_max_distance = -1
    #distance_map = {(item): abs(item[0] - item[1]) for item in itertools.permutations(range(1, n+1), 2)}
    #s = time.time()
    for p in permutations(n):
        distance_list = [abs(p1 - p2) for p1, p2 in itertools.izip(p, p[1:])]
        md = min(distance_list)
        if current_max_distance == md:
            maximal_distances.append(p)
        elif current_max_distance < md:
            current_max_distance = md
            maximal_distances = [p]
    #print time.time() - s
    #print len(maximal_distances)
    #print maximal_distances
    return maximal_distances

for t in range(int(raw_input())):
    n, k = [int(i.strip()) for i in raw_input().split() if i.strip()]
    
    if n <= 1 and k <= 1:
        print 1
    elif n <= 1 and k > 1:
        print -1
    else:
        maximal_distances = get_maximal_distance(n)
        if k <= 0 or len(maximal_distances) < k:
            print -1
        else:
            print " ".join([str(i) for i in maximal_distances[k-1]])
