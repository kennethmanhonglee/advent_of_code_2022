from typing import List

class Day1Attempt():
  def __init__(self) -> None:
    print(self.part_1())
    print(self.part_2())

  def part_1(self) -> int:
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

  def part_2(self) -> List[int]:
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

Day1Attempt()
