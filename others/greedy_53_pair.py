
def possible_values_53(num):
    # 0 index for 5s
    # 1 index for 3s

    possible_values = [(num, 0)] # all 5s
    min5 = 3
    min3 = 5
    i = min3
    while i < num:
        max5 = num - i
        if max5 % min5 == 0:
            possible_values.append((max5, (num-max5)))
        i += min3
    possible_values.append((0, num)) 
    return possible_values

def greedy(num):
    pv = possible_values_53(num)
    for f, t in pv:
        greedy_five = 5*f
        greedy_three = 3*t
        greedy_num = ""
        if greedy_five > 0 and greedy_five % 3 == 0 and greedy_five % 5 == 0:
            greedy_num += "5"*f
        if greedy_three > 0 and greedy_three % 3 == 0 and greedy_three % 5 == 0:
            greedy_num += "3"*t
        #print f, t, greedy_five, greedy_three, greedy_num
        if greedy_num:
            return greedy_num

for t in xrange(int(raw_input())):
    num = int(raw_input())
    if num <= 2:
        print -1
    else:
        n = greedy(num)
        if n:
            print n
        else:
            print -1
