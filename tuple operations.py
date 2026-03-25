
# Create tuple with mixed data types
t = (10, 20, "Python", 10, 25.5)

print("\nOriginal Tuple:", t)

# 1. Find index of element
x = 10
print("\nIndex of", x, "is:", t.index(x))

# 2. Count occurrences
print("Count of", x, "is:", t.count(x))

# 3. Convert tuple to list, modify, and convert back
l = list(t)
l.append("Yadnesh")

new_tuple = tuple(l)

print("\nList after adding element:", l)
print("New Tuple:", new_tuple)

print("Name: Yadnesh Wagaskar")
print("Roll No: 25FC131")
print("Batch: F2")

""" Output:

Original Tuple: (10, 20, 'Python', 10, 25.5)

Index of 10 is: 0
Count of 10 is: 2

List after adding element: [10, 20, 'Python', 10, 25.5, 'Yadnesh']
New Tuple: (10, 20, 'Python', 10, 25.5, 'Yadnesh')
Name: Yadnesh Wagaskar
Roll No: 25FC131
Batch: F2"""