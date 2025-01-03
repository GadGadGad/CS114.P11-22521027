import sys
import math
# Code nay em lay y tuong tu trong lab cua coursera
# Em co gap tinh trang bi tran so, nen em co prompt thu chatGPT cach fix,
# 'Gradient Descent Overflow error with x and y: ...'. Em thay co cach la scale lai X va Y nen em ap dung 
data = sys.stdin

X = []
Y = []

for line in data:
    x, y = line.strip().split(",")
    X.append(int(x))
    Y.append(float(y))

def calculate_mse(X, Y, a, b):
    n = len(X)
    mse_sum = 0.0
    for i in range(n):
        y_pred = a * X[i] + b
        mse_sum += (Y[i] - y_pred) ** 2
    mse = mse_sum / n
    return mse

def normalize(data):
    mean = sum(data) / len(data)
    std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    return [(x - mean) / std for x in data], mean, std

X_norm, X_mean, X_std = normalize(X)
Y_norm, Y_mean, Y_std = normalize(Y)

def gradient(X, Y, a, b):
    n = len(X)
    dL_da = 0
    dL_db = 0
    for i in range(n):
        y_pred = a * X[i] + b
        dL_da += (y_pred - Y[i]) * X[i]
        dL_db += y_pred - Y[i]
    dL_da /= n
    dL_db /= n
    return dL_da, dL_db

def gradient_descent(X, Y, a, b, alpha, num_iters, gradient_function):
    for _ in range(num_iters):
        dL_da, dL_db = gradient_function(X, Y, a, b)
        a = a - alpha * dL_da
        b = b - alpha * dL_db
    return a, b

a_init = 0
b_init = 0
iterations = 1
tmp_alpha = 1

a_final_norm, b_final_norm = gradient_descent(X_norm, Y_norm, a_init, b_init, tmp_alpha, iterations, gradient)

a_final = a_final_norm * (Y_std / X_std)
b_final = Y_mean + b_final_norm * Y_std - a_final * X_mean
print(a_final, b_final)

