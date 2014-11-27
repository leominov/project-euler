r = range(1, 101)
print sum(r) ** 2 - sum(i ** 2 for i in r)
