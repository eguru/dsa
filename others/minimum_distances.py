


n = int(raw_input().strip())
index_map = {}

for i, a in enumerate(raw_input().strip().split(' ')):
    index_map.setdefault(a, []).append(i)

min_list = []
for a in index_map:
    if len(index_map[a]) > 1:
        ai = index_map[a][0]
        for aj in index_map[a][1:]:
            min_list.append(abs(ai - aj))
if min_list:
    print min(min_list)
else:
    print -1
        
