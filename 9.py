for a in range(1, 1000):
    for b in range(1, a-1):
        c = 1000-a-b
        if c == (a**2 + b**2)**0.5:
            print(a*b*c)
