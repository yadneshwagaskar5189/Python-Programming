numbers = [10,20,30,40,50]
numbers.append(60)
print(numbers)
numbers.insert(45,80)
print(numbers)
numbers.remove(30)
print(numbers)
numbers.pop(3)
print(numbers)
del numbers[0]
print(numbers)
numbers[1]=15
print(numbers)

num=[40,5,23,60]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(max(num))
print(min(num))
print(sum(num))

num=[10,20,40,20,33,43,53,43,33]
unique_list=[]
for i in num:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

number=[10,20,30,40,60]
list=number[1:4]
print(list)
list=number[0:5:2]
print(list)
list=number[::-1]
print(list)

print("Name: Yadnesh Wagaskar")
print("Roll No: 25FC131")
print("Batch: F2")

""" Output:
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60, 80]
[10, 20, 40, 50, 60, 80]
[10, 20, 40, 60, 80]
[20, 40, 60, 80]
[20, 15, 60, 80]
[5, 23, 40, 60]
[60, 40, 23, 5]
60
5
128
[10, 20, 40, 33, 43, 53]
[20, 30, 40]
[10, 30, 60]
[60, 40, 30, 20, 10]
Name: Yadnesh Wagaskar
Roll No: 25FC131
Batch: F2 """