################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list

print("Exercise 3.1")

s = 0
for a in lst:
    s += a
print(s)

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")

s = 1
for a in lst:
    s *= a
print(s)

print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

s = 0
for a in lst:
    s += a**2
print(s)

print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

s = lst[0]
for a in lst:
    if a > s:
        s = a
print(s)

print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.5")

print("same question ??")

print("---")