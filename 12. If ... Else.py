# ========================Python Conditions and If statements=========================
a = 33
b = 200
if b > a:
    print("b i greater than a")

# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose                                                                                                                     

# =================================Elif======================================
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".\
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".
  
# ==================================Else=====================================
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#  In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

# You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#  SHORT HAND
#  Short Hand If
a = 200
b = 33

if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#   Or
# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#   Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#   Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")