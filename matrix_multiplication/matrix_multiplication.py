import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
b = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
# M(row * column) = M[0] * M[0]
size_of_a = f"{len(a)} x {len(a[0])}"
size_of_b = f"{len(b)} x {len(b[0])}"

print(f"a is a {size_of_a} matrix")
print(f"b is a {size_of_b} matrix")

# result of a * b
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

result = [
    [sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*b)] for X_row in a
]

# or

result = np.dot(a, b)
print(np.array(result))
