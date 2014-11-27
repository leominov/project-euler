i, n, s = 1, 0, 0

while i < 4000000:
    i, n = i+n, i
    if i % 2 == 0:
        s += i

print(s)
