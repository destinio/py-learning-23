people = ["destin", "stacy"]
people.insert(2, "everett")
people.append("ellis")

cats = ["willie", "jimi"]

people.extend(cats)

print(people)

cars = ["van", "rav", "other"]
cars.remove("rav")
cars.pop(-1)

# ['van']
print(cars)

for v in people:
  print(v.upper())

# index
for i in range(len(people)):
  print(i)

i = 0 

while i < len(people):
  # print(list(people[i]))
  # print([p for p in people[i]])

  print([*people[i]])

  i = i + 1

#https://www.w3schools.com/python/python_lists_methods.asp
new_people = people.copy()
new_new_people = list(new_people)

new_people.sort()
new_people.reverse()

print(new_new_people)
print(new_people)