n = 0
for a in range(100, 1000):
    for b in range(100, a+1):
        x = a*b
        s = str(x)
        if x > n and s == s[::-1]:
            n = x

print n
