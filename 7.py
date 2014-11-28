def check(n):
    for i in range(int(n ** 0.5)):
        if n % (i + 2) == 0:
            return False
    return True

n = 1
for k in range(10001):
    while check(n) == False:
        n += 1
    n += 1

n -= 1
print(n)
