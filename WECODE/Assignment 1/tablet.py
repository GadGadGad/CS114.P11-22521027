import math
n = int(input())

cnt = 0
# n^2 = a^2 + b^2 >= 2b^2
# => n >= b * sqrt{2}
# => b <= n / sqrt{2}
n_square = n ** 2
for b in range(1, int(n / math.sqrt(2)) - 1):
    tmp = n_square - b ** 2
    if math.sqrt(tmp).is_integer():
        cnt += 1

print(cnt)