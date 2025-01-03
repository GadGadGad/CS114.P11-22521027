import sys
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Simulate stdin data (replace sys.stdin if using real input)
data = sys.stdin  # Placeholder; replace with actual data or file reading as needed

# Initialize data lists
X = []
Y = []

# Read input data
for line in data:
    x, y = line.strip().split(",")
    X.append(int(x))
    Y.append(float(y))

# Mean Squared Error (MSE) calculation function
def calculate_mse(X, Y, a, b):
    n = len(X)
    mse_sum = 0.0
    for i in range(n):
        y_pred = a * X[i] + b
        mse_sum += (Y[i] - y_pred) ** 2
    mse = mse_sum / n
    return mse

# Data normalization function
def normalize(data):
    mean = sum(data) / len(data)
    std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    return [(x - mean) / std for x in data], mean, std

# Normalize the data
X_norm, X_mean, X_std = normalize(X)
Y_norm, Y_mean, Y_std = normalize(Y)

# Gradient calculation function for gradient descent
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

# Gradient descent function
def gradient_descent(X, Y, a, b, alpha, num_iters, gradient_function):
    for _ in range(num_iters):
        dL_da, dL_db = gradient_function(X, Y, a, b)
        a = a - alpha * dL_da
        b = b - alpha * dL_db
    return a, b

# Initialize values for gradient descent
a_init = 0
b_init = 0
iterations = 5
tmp_alpha = 1

# Perform gradient descent on normalized data
a_final_norm, b_final_norm = gradient_descent(X_norm, Y_norm, a_init, b_init, tmp_alpha, iterations, gradient)

# Denormalize the final coefficients to match original data
a_final = a_final_norm * (Y_std / X_std)
b_final = Y_mean + b_final_norm * Y_std - a_final * X_mean

# Manual calculation using normal equations
n = len(X)
sum_x = sum(X)
sum_y = sum(Y)
sum_x_squared = sum(i**2 for i in X)
sum_xy = sum(i*j for i, j in zip(X, Y))

# Calculate the slope (a2) and intercept (b2) using normal equations
a2 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b2 = (sum_y - a2 * sum_x) / n

# Use LinearRegression from sklearn to get a1 and b1
X_reshaped = np.array(X).reshape(-1, 1)  # Reshape X for sklearn

# Create and fit the model
model = LinearRegression()
model.fit(X_reshaped, Y)

# Get coefficients
a1 = model.coef_[0]  # Slope (a1)
b1 = model.intercept_  # Intercept (b1)

a0 = 1.0157358e-07
b0 = -0.40155127822067227

# Calculate MSE for each set of coefficients
mse0 = calculate_mse(X, Y, a0, b0)
mse1 = calculate_mse(X, Y, a1, b1)
mse2 = calculate_mse(X, Y, a2, b2)
mse_final = calculate_mse(X, Y, a_final, b_final)

# Print MSE values
print(f'MSE for line 0 (test case): {mse0}')
print(f'MSE for line 1 (library-based): {mse1}')
print(f'MSE for line 2 (manual calculation): {mse2}')
print(f'MSE for gradient descent line: {mse_final}')

# Plot results
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='blue', label='Original Data')

# Values for plotting the lines
x_values = [min(X), max(X)]
y_pred_0 = [a0 * x + b0 for x in x_values]
y_pred_final = [a_final * x + b_final for x in x_values]
y_pred_1 = [a1 * x + b1 for x in x_values]
y_pred_2 = [a2 * x + b2 for x in x_values]

# Plot all the lines
plt.plot(x_values, y_pred_0, '.', label='Test Case Line')
plt.plot(x_values, y_pred_final, color='red', label='Gradient Descent Line')
plt.plot(x_values, y_pred_1, color='green', label='Library-based Line (Line 1)')
plt.plot(x_values, y_pred_2, color='orange', label='Normal Equation Line (Line 2)')

# Finalize plot
plt.title('Regression Lines Comparison')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()

# Save the plot to a file
plt.savefig('regression_lines_comparison_updated.png')
plt.close()

# Output final coefficients
print(f'Final coefficients from Test case (Line 0): a = {a0}, b = {b0}')
print(f'Final coefficients from Library (Line 1): a = {a1}, b = {b1}')
print(f'Final coefficients from Normal Equation (Line 2): a = {a2}, b = {b2}')
print(f'Final coefficients from Gradient Descent: a = {a_final}, b = {b_final}')
