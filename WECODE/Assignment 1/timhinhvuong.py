A = input().split()
B = input().split()

def toTuple(A):
    list_A = []
    for num in A:
        list_A.append(int(num))
    tuple_A = (list_A[0], list_A[1])
    return tuple_A 

A = toTuple(A)
B = toTuple(B)
vectorAB = (B[0] - A[0], B[1] - A[1])

# 2 vector vuong goc co tich vo huong = 0 => xAB * xCD + yAB * yCD = 0
# => CD = (-xAB, yAB) hoặc (xAB, -yAB)
# https://loigiaihay.com/ly-thuyet-tich-vo-huong-cua-hai-vecto-c45a4971.html
vectorCD1 = (-vectorAB[1], vectorAB[0])
vectorCD2 = (vectorAB[1], -vectorAB[0])

C1 = (B[0] + vectorCD1[0], B[1] + vectorCD1[1])
C2 = (B[0] + vectorCD2[0], B[1] + vectorCD2[1])

D1 = (A[0] + vectorCD1[0], A[1] + vectorCD1[1])
D2 = (A[0] + vectorCD2[0], A[1] + vectorCD2[1])
# Phan nay tro xuong em dua tren  https://www.desmos.com/calculator?lang=vi
def checkAB(A, B):
    # If A is on the left of B
    if(A[0] < B[0]):
        return -1
    # If A is on the right of B
    elif (A[0] > B[0]):
        return 1

    # If A and B have same x value, A below B
    if(A[1] < B[1]):
        return -1
    # Same, but A above B
    elif (A[1] > B[1]):
        return 1
    # Else, A = B
    return 0

if checkAB(A, B) == 1:
    print(A, D1, C1, B)
    print(A, B, C2, D2)
elif checkAB(A, B) == -1:
    print(A, D1, C1, B)
    print(A, B, C2, D2)