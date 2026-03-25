# Create two matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("\nMatrix A:", A)
print("Matrix B:", B)

# 1. Addition
add = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        add[i][j] = A[i][j] + B[i][j]

print("\nAddition:", add)

# Subtraction
sub = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        sub[i][j] = A[i][j] - B[i][j]

print("Subtraction:", sub)

# 2. Transpose of A
transpose = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        transpose[j][i] = A[i][j]

print("\nTranspose of Matrix A:", transpose)

# 3. Multiplication
mul = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            mul[i][j] += A[i][k] * B[k][j]

print("\nMultiplication:", mul)

# 4. Check symmetric (A == transpose of A)
if A == transpose:
    print("\nMatrix A is Symmetric")
else:
    print("\nMatrix A is Not Symmetric")

    

print("Name: Yadnesh Wagaskar")
print("Roll No: 25FC131")
print("Batch: F2")


""" Output:
Matrix A: [[1, 2], [3, 4]]
Matrix B: [[5, 6], [7, 8]]

Addition: [[6, 8], [10, 12]]
Subtraction: [[-4, -4], [-4, -4]]

Transpose of Matrix A: [[1, 3], [2, 4]]

Multiplication: [[19, 22], [43, 50]]

Matrix A is Not Symmetric
Name: Yadnesh Wagaskar
Roll No: 25FC131
Batch: F2"""