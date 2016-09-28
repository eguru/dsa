import math

def get_next_prime(curr):
    if not curr or curr <= 1:
        return 2
    elif curr == 2:
        return 3
    else:
        def isPrime(n):
            for i in range(2, int(math.sqrt(n)+1)):
                if n % i == 0: 
                    return False;
            return n>1;
        for n in range(curr+2, 10000):
            if isPrime(n):
                return n

def get_p_piles(p, dplates, ndplates):
    dp = []
    ndp = []
    for pile in ndplates:
        if int(pile) % p == 0:
            dp.append(pile)
        else:
            ndp.append(pile)
    dplates.extend(dp)
    return ndp

n, q = [int(i.strip()) for i in raw_input().split() if i.strip()]
piles = [i.strip() for i in raw_input().split() if i.strip()]
dplates = []
ndplates = piles
p = 1
for i in range(q):
    p = get_next_prime(p)
    ndplates = get_p_piles(p, dplates, ndplates)
    if not ndplates:
        break

print "\n".join(dplates + ndplates)


