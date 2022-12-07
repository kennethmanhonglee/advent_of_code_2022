
def day_1_part_1():
  total = 0
  highest = 0

  with open('./input.txt') as file:
    for line in file:
      if line == "\n":
        highest = max(highest, total)
        total = 0
      else:
        total += int(line)

  return highest

print(day_1_part_1())

def day_2_attempt():
  total = 0
  sums = []

  with open('./input.txt') as file:
    for line in file:
      if line == '\n':
        sums.append(total)
        total = 0
      else:
        total += int(line)
  
  return sum(sorted(sums, reverse=True)[:3])
    
print(day_2_attempt())