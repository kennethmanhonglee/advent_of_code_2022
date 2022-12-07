total = 0
highest = 0

with open('./input.txt') as file:
  for line in file:
    if line == "\n":
      highest = max(highest, total)
      total = 0
    else:
      total += int(line)

print(highest)