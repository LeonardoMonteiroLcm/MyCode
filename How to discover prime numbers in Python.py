a1 = 1
n = 100

print("Determine all prime numbers beteween %d and %d" % (a1, n))

print("\nMethod 1:")
nprimes = 0
for i in range(a1, n):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        print("%d is a prime number" % (i))
        nprimes += 1
print("Total = %d" % (nprimes))

print("\nMethod 2:")
nprimes = 0
for i in range(a1, n):
    isprime = True
    for j in range (2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        print("%d is a prime number" % (i))
        nprimes += 1
print("Total = %d" % (nprimes))
