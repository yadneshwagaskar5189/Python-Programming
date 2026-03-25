# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)

# 1. Union
print("\nUnion:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 2. Subset and Superset check
print("\nSubset check:", set1.issubset(set2))
print("Superset check:", set1.issuperset(set2))

# 3. Remove duplicate elements from list
list1 = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list1)

print("\nOriginal List:", list1)
print("List after removing duplicates:", set_from_list)

# 4. Find common elements between two lists
list2 = [3, 4, 4, 5, 6]
common = set(list1).intersection(set(list2))

print("\nSecond List:", list2)
print("Common elements:", common)

print("Name: Yadnesh Wagaskar")
print("Roll No: 25FC131")
print("Batch: F2")

""" Output:
Set 1: {1, 2, 3, 4, 5}
Set 2: {4, 5, 6, 7, 8}

Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference (set1 - set2): {1, 2, 3}
Symmetric Difference: {1, 2, 3, 6, 7, 8}

Subset check: False
Superset check: False

Original List: [1, 2, 2, 3, 4, 4, 5]
List after removing duplicates: {1, 2, 3, 4, 5}

Second List: [3, 4, 4, 5, 6]
Common elements: {3, 4, 5}
Name: Yadnesh Wagaskar
Roll No: 25FC131
Batch: F2"""