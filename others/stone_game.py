
def remove_stones(player, stones):
    if stones <= 2:
        stones -= 2
    elif stones == 3:
        stones -= 3
    elif stones == 4:
        stones -= 3
    elif stones == 5:
        stones -= 5
    else: # > 5
        # if n - 2 or n - 3 or n - 5, which ever give < 2 move that
        # else which ever give > 5 move that
        if  (stones - 2) < 2:
            stones -= 2
        elif (stones - 3) < 2: 
            stones -= 3
        elif (stones - 5) < 2:
            stones -= 5
        else:
            # try to bring stones to 7K or 7K + 1 where
            if (stones-2) % 7 == 0 or (stones-2) % 7 == 1:
                stones -= 2
            elif (stones-3) % 7 == 0 or (stones-3) % 7 == 1:
                stones -= 3
            elif (stones-5) % 7 == 0 or (stones-5) % 7 == 1:
                stones -= 5
            else:
                stones -= 2
                
    return stones

for t in xrange(int(raw_input())):
    stones = int(raw_input())
    p1 = "First"
    p2 = "Second"    
    winner = ""    
    game_over = False

    move = 1
    while not game_over:
        player = p1
        if move % 2 == 0:
            player = p2
        #print player, stones, " === before"
        stones = remove_stones(player, stones)
        #print player, stones, " === after"
        if stones < 0:
            game_over = True
            if player == p2:
                winner = p1
            else:
                winner = p2
        else:
            move += 1

    if game_over:
        print winner
