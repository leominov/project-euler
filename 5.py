import sys

d = range(1, 21)
for i in xrange(2520, sys.maxint, 20):
    k = 0
    for n in d:
        if i % n == 0:
            k += 1
    if k == 20:
        break

print(i)
