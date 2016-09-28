
l = [[raw_input().strip(), float(raw_input().strip())] for i in range(int(raw_input()))]
marks = []
for name, mark in l:
    marks.append(mark)
marks.sort()
lowest = marks[0]
i = 1
while lowest == marks[i]:
    i += 1
second_lowest = marks[i]
print "\n".join(sorted([name for name, marks in l if marks == second_lowest]))

