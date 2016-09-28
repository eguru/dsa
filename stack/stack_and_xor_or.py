
def bitwise_calculate(x, y):
    return (((x & y) ^ (x | y)) & (x ^ y))

print bitwise_calculate(6, 9)
