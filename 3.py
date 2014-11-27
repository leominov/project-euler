l_factor, p, n = 1, 3, 600851475143
    
while n % 2 == 0:
    l_factor = 2
    n = n/2

while n != 1:
    while n % p == 0:
        l_factor = p
        n = n/p
    p += 2

print(l_factor)
