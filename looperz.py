people = ["destin", "stacy", "everett", "ellis"]
for v in people:
  print(v)


# for i in range(len(people)):
#   print(i)

for i in range(0, 101, 5):
  print(i)

for v in people:
  if v == "everett": continue

  print(v.upper())
else:
  print("the people have been uppereded")