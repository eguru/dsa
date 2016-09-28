x = int(raw_input().strip())
y = int(raw_input().strip())
z = int(raw_input().strip())
n = int(raw_input().strip())

print [[xi, yi, zi] for xi in range(x+1) for yi in range(y+1) for zi in range(z+1) if (xi+yi+zi) != n]
