import pandas as pd
import os
import numpy as np


A = np.random.randint(0, 21, (3, 3))
B = np.random.randint(0, 21, (3, 3))

addition_result = A + B

multiplication_result = np.dot(A, B)

transpose_result = multiplication_result.T

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix Addition:\n", addition_result)
print("\nMatrix Multiplication:\n", multiplication_result)
print("\nTranspose of Product Matrix:\n", transpose_result)