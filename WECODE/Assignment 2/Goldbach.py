import math

# Code lay y tuong tu: https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def SieveOfEratothenes(n):
    prime = [0 for i in range(n + 1)]
    for p in range (2, int(math.sqrt(n)) + 1):
        if(prime[p] == 0):
            for i in range(p * p, n + 1, p):
                prime[i] = 1
    p += 1
    
    return prime
n = int(input())

idx = SieveOfEratothenes(n)
prime = [i for i in range(2, len(idx)) if idx[i] == 0]
cnt = 0

# for i in range(len(siever)):
#     if(siever[i] == 1):
#         print(i)

for i in prime:
    for j in prime:
        if i + j == n and i <= j:
            # print(f"{i}, {j}")
            cnt += 1
print(cnt)
