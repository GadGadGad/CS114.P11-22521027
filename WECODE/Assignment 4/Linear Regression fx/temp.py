import sys
import math

X = []
Y = []
data = sys.stdin
# Em va ban Le Minh Nhut co trao doi y tuong va chia se nhieu nguon kien thuc cho nhau
# Bai nay em co nghi toi phuong phap giai he phuong trinh bac 3 de dat mse thap hon thang y = ax + blogx + c dua vao cach lam bai truoc
# cua ban Le Minh Nhut voi y = ax + b, thi o bai nay y = ax^4 + bx^2 + cx + d
for line in data:
    x, y = line.strip().split(",")
    X.append(float(x))
    Y.append(float(y))


def calculate_mse(X, Y, a, b, c, d):
    n = len(X)
    mse_sum = 0.0
    for i in range(n):
        y_pred = a * X[i] ** 4 + b * X[i] ** 2 + c * X[i] + d
        mse_sum += (Y[i] - y_pred) ** 2
    mse = mse_sum / n
    return mse

# Code nay em lay y tuong o day: https://stackoverflow.com/questions/63766815/determinate-of-a-singular-4x4-matrix-is-non-zero-using-numpy-det
def determinant(m1): 
    if(len(m1) == 3):
        a = m1[0][0] * (m1[1][1] * m1[2][2] - m1[2][1] * m1[1][2]) 
        b = m1[0][1] * (m1[1][0] * m1[2][2] - m1[2][0] * m1[1][2]) 
        c = m1[0][2] * (m1[1][0] * m1[2][1] - m1[2][0] * m1[1][1])                     
        return(a-b+c)     
    elif (len(m1) == 4):
        a1 = 0
        a2 = 0
        a3 = 0 
        a4 = 0   
        a1 = m1[0][0] * (m1[1][1] * (m1[2][2] * m1[3][3] - m1[3][2] * m1[2][3]) - m1[1][2] * (m1[2][1] * m1[3][3] - m1[3][1] * m1[2][3]) + m1[1][3] * (m1[2][1] * m1[3][2] - m1[3][1] * m1[2][2]))
        a2 = m1[0][1] * (m1[1][0] * (m1[2][2] * m1[3][3] - m1[3][2] * m1[2][3]) - m1[1][2] * (m1[2][0] * m1[3][3] - m1[3][0] * m1[2][3]) + m1[1][3] * (m1[2][0] * m1[3][2] - m1[3][0] * m1[2][2])) 
        a3 = m1[0][2] * (m1[1][0] * (m1[2][1] * m1[3][3] - m1[3][1] * m1[2][3]) - m1[1][1] * (m1[2][0] * m1[3][3] - m1[3][0] * m1[2][3]) + m1[1][3] * (m1[2][0] * m1[3][1] - m1[3][0] * m1[2][1])) 
        a4 = m1[0][3] * (m1[1][0] * (m1[2][1] * m1[3][2] - m1[3][1] * m1[2][2]) - m1[1][1] * (m1[2][0] * m1[3][2] - m1[3][0] * m1[2][2]) + m1[1][2] * (m1[2][0] * m1[3][1] - m1[3][0] * m1[2][1]))
    return a1 - a2 + a3 -a4   

def transpose(matrix):
    return [[matrix[j][i] for j in range(4)] for i in range(4)]

# Em co prompt chatgpt cach tim ma tran he so: Prompt voi ChatGPT-4o:
# "How to calculate a 4x4 cofactor matrix in python without using numpy"
def cofactor(matrix):
    cof_matrix = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            temp_matrix = []
            for row in range(4):
                if row != i:
                    temp_row = []
                    for col in range(4):
                        if col != j:
                            temp_row.append(matrix[row][col])
                    temp_matrix.append(temp_row)

            cof_matrix[i][j] = determinant(temp_matrix)
            if (i + j) % 2 != 0:
                cof_matrix[i][j] = -cof_matrix[i][j]
    return cof_matrix

def inverse(matrix):
    det = determinant(matrix)

    cof_matrix = cofactor(matrix)
    adj_matrix = transpose(cof_matrix)
    inverse_matrix = [[adj_matrix[i][j] / det for j in range(4)] for i in range(4)]

    return inverse_matrix

def dot(m, v):
    return [sum(m[i][j] * v[j] for j in range(4)) for i in range(4)]

def solve_linear(X, Y):
    X_temp = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    
    Y_temp = [0, 0, 0, 0]

    for i in range(len(X)):
        x_i = X[i]
        y_i = Y[i]

        X_temp[0][0] += x_i ** 8
        X_temp[0][1] += x_i ** 6
        X_temp[0][2] += x_i ** 5
        X_temp[0][3] += x_i ** 4

        X_temp[1][0] += x_i ** 6
        X_temp[1][1] += x_i ** 4
        X_temp[1][2] += x_i ** 3
        X_temp[1][3] += x_i ** 2

        X_temp[2][0] += x_i ** 5
        X_temp[2][1] += x_i ** 3
        X_temp[2][2] += x_i ** 2
        X_temp[2][3] += x_i

        X_temp[3][0] += x_i ** 4
        X_temp[3][1] += x_i ** 2
        X_temp[3][2] += x_i
        X_temp[3][3] += 1

        Y_temp[0] += y_i * x_i ** 4
        Y_temp[1] += y_i * x_i ** 2
        Y_temp[2] += y_i * x_i
        Y_temp[3] += y_i

    sol = tuple(dot(inverse(X_temp), Y_temp))

    return sol

sol = solve_linear(X, Y)

print(f"{sol[0]}*x**4 + {sol[1]}*x**2 + {sol[2]}*x + {sol[3]}")
# print(calculate_mse(X, Y, sol[0], sol[1], sol[2], sol[3]))