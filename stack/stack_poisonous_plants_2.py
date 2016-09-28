n = int(raw_input().strip())
plants = [int(i.strip()) for i in raw_input().split() if i.strip()]

stack = []       
i = len(plants) - 1
while i > 0:
    if plants[i-1] > plants[i]:
        stack.append(plants[i])
    i -= 1
stack.append(plants[0])
day = 1

def remove_dead_plant(plants):
    found_dead = True
    stack = []       
    i = len(plants) - 1
    while i > 0:
        if plants[i-1] < plants[i]:
            found_dead = True
            plants.pop(i)
        i -= 1
    if not found_dead:
        return []
    return stack

while stack:
    stack.reverse()
    print stack
    stack = remove_dead_plant(stack)
    print stack
    day += 1
    
print stack, day

"""
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
"""
