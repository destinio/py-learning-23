print(123)

first_name = "destin"
age = 38
excited = True

# this is a comment add it is awesome

"""
this is a milti
line comment
"""

print(first_name, age, excited)

# Casting
# does not seem to work

x = str(age)

print(type(str(age)))

print(float(age))

a, b, c = 1,2,3

print(a, b, c)

people = ["destin", "stacy"]

destin, stacy = people

for v in people:
  print(len(v))

a_string = "this is a string thing a ding"

print("string" in a_string)
print("ellis" in people)
print("destin is in the people array", "destin" in people)

if "stacy" in people:
  print("stacy is int the people arr")

if "everett" not in people:
  print("everett is not in the people array")

people_slice = people[0:len(people)]

print(people_slice)