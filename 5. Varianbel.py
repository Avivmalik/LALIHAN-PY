# Variable adalah tempat menyimpan data 

# PYTHON VARIABLE
# assignmnet nilai
x = 10
y = "John"
print(x)
print(y)

#casting type data
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# get the type
x = 5
y = "John"
print(type(x))
print(type(y))

# variable name are case sensitive
a =4
A ="syafii"
# A will not overwrite a

# Variable Names :

    # Legal variable names:
    # myvar = "John"
    # my_var = "John"
    # _my_var = "John"
    # myVar = "John"
    # MYVAR = "John"
    # myvar2 = "John"

    # Illegal variable names:
    # 2myvar = "John"
    # my-var = "John"
    # my var = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

