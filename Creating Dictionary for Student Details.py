student = {
    "Name": "Arryan",
    "Roll No": "25FC434",
    "Marks": 85
}
print("\nOriginal Dictionary:")
print(student)
# 1. Add a new key-value pair
student["Batch"] = "F11"
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
