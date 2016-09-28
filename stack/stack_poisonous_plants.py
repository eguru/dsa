n = int(raw_input().strip())
plants = [int(i.strip()) for i in raw_input().split() if i.strip()]

stack = []
max_days = 0
dead_plant_found = True
i = len(plants)
days = 0
while i > 1:
    r = i - 1
    l = r - 1
    print "if plants[l] >= plants[r] = ", plants[l], plants[r]
    if plants[l] > plants[r]:
        stack.append(plants[r])
        print "In if"
    else:
        # ignore if current left value is bigger than it's left
        if plants[l] < plants[l-1]:
            if l == 0 and stack:
                if stack[-1] > plants[l]:
                    stack.pop()
            if stack:
                print "while stack and stack[-1] > plants[l]: ", stack, stack[-1], plants[l]
            while stack and stack[-1] > plants[l]:
                print "In while"
                days += 1
                stack.pop()
    i -= 1

if len(stack) == len(plants) -1 :
    days = 0
else:
    days += 1
print days



dead_plants = 1
days = 0
while dead_plants:
    dead_plants = 0
    j = len(plants) - 1
    while j >= 1:
        #print plants, plants[j], plants[j-1]
        if plants[j-1] < plants[j]:
            dead_plants += 1
            plants.pop(j)
        j -= 1
    print plants
    days += 1

print days - 1
     
