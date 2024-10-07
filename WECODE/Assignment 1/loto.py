A = []
checked = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    temp = input()
    A.append([int(num) for num in temp.split()])

# print(A)
N = int(input())


while N > 0:
    N -= 1
    pick = int(input())
    for i in range(3):
        for j in range(3):
            if(A[i][j] == pick):
                checked[i][j] = 1

# print(checked)

def checkWin(checked):
    for row in checked:
        if all(row): 
            return True
    for col in range(3):
        if all(checked[row][col] for row in range(3)):  
            return True
    # Cai nay em hoi chatgpt cach kiem tra duong cheo chinh
    if all(checked[i][i] for i in range(3)):
        return True
    # Cai nay em cung hoi chat gpt kiem tra duong cheo chinh nguoc lai
    if all(checked[i][2 - i] for i in range(3)): 
        return True

    return False

res = "Yes" if checkWin(checked) else "No"
print(res)