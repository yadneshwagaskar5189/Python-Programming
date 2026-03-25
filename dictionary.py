# Create dictionary with student details
student = {
    "Name": "Yadnesh",
    "Roll No": "25FC131",
    "Marks": 85
}

print("\nOriginal Dictionary:")
print(student)

# 1. Add a new key-value pair
student["Batch"] = "F2"
print("\nDictionary after adding Batch:")
print(student)

# Update value
student["Marks"] = 90
print("\nDictionary after updating Marks:")
print(student)

# Delete key-value pair
del student["Batch"]
print("\nDictionary after deleting Batch:")
print(student)

# 2. Iterate through keys, values, and items
print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# 3. Word frequency count
text = "python is easy and python is powerful"

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")
print(frequency)

print("Name: Yadnesh Wagaskar")
print("Roll No: 25FC131")
print("Batch: F2")

""" Output:
Original Dictionary:
{'Name': 'Yadnesh', 'Roll No': '25FC131', 'Marks': 85}

Dictionary after adding Batch:
{'Name': 'Yadnesh', 'Roll No': '25FC131', 'Marks': 85, 'Batch': 'F2'}

Dictionary after updating Marks:
{'Name': 'Yadnesh', 'Roll No': '25FC131', 'Marks': 90, 'Batch': 'F2'}

Dictionary after deleting Batch:
{'Name': 'Yadnesh', 'Roll No': '25FC131', 'Marks': 90}

Keys:
Name
Roll No
Marks

Values:
Yadnesh
25FC131
90

Key-Value pairs:
Name : Yadnesh
Roll No : 25FC131
Marks : 90

Word Frequency:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
Name: Yadnesh Wagaskar
Roll No: 25FC131
Batch: F2 """
