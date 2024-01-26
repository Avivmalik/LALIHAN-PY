# ==========================Python Assignment Operators===============================
x = 5
x += 3
print(x)

# berlaku juga untuk pengurangan, perkalian, pembagian, eksponen,modulus, floor

# ============================Python Bitwise Operators===========================
# Performs Bitwise AND on operands and assign value to left operand
x = 5
x &= 3 # x = x & 3 -> x = 5 & 3
print(x)

# Performs Bitwise OR on operands and assign value to left operand
x = 5
x |= 3
print(x)

# Performs Bitwise xOR on operands and assign value to left operand
x = 5
x ^= 3
print(x)

# Performs Bitwise right shift on operands and assign value to left operand
x = 5
x >>= 3
print(x)

# Performs Bitwise left shift on operands and assign value to left operand
x = 5
x <<= 3
print(x)


# ==============================Python Comparison Operators==============================
	# Equal
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

    # Not equal 
x = 5
y = 3
print(x != y)
    # Greater than/Less than, Greater than or equal ">="/Less than or equal "<="
x = 5
y = 3

print(x > y)
# returns True because 5 is greater than 3

# =============================Python Logical Operators=============================
# And: Returns True if both statements are true
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# or: Returns True if one of the statements is true
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# Not: Reverse the result, returns False if the result is true
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

# =============================Python Membership Operators==============================

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list