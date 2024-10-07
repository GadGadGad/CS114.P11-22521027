import sys
from decimal import Decimal, getcontext

# Bai nay em co hoi ban Minh Nhut MSSV: 22521060 ve cach xu ly so lon va da duoc ban huong dan cach su dung thu vien 
# Decimal

getcontext().prec = 15001

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def reverseAndAddProcess(n):
    return n + Decimal(str(n)[::-1])

n = Decimal(sys.stdin.readline().strip())

temp = n
res = []
sys.stdout.flush()

for i in range(10001):
    if isPalindrome(temp):
        sys.stdout.write("NO\n")
        sys.stdout.write("\n".join(map(str, res)) + "\n") 
        break
    
    temp = reverseAndAddProcess(temp)
    res.append(temp)

    if len(str(temp)) > 15000:
        sys.stdout.write(f"YES\n{i + 1} {temp}\n")
        break
else:
    sys.stdout.write(f"YES\n10001 {temp}\n")
