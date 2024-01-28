# ==========================================List========================================

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

# cara alternatif membuat list
data = range (0,11,2) #range(start,stop,step)
data_list = list(data)
print (data_list)

# Membuat list dengan for loop, list comprehension
list_for = [i for i in range (0,11)]
print (list_for)

list_for = [i **3 for i in range (0,11)]
print (list_for)

# list menggunakan if
List_if = [i for i in range (0,11) if i !=5] #skip angka 5
print (List_if)

List_if = [i for i in range (0,11) if i %2 ==0] # genap (hasil bagi/modulus menggunkan 2 adalah 0)
print (List_if)

List_if = [i for i in range (0,11) if i %2 !=0] # ganjil (hasil bagi/modulus menggunkan 2 adalah bukan 0)
print (List_if)
# ==========================Access List Items================================


