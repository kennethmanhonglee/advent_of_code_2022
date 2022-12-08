import re

class Day5Attempt():
  STACKS = [
    None,
    ['H', 'T', 'Z', 'D'],
    ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],
    ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],
    ['L', 'C', 'N', 'F', 'H', 'Z'],
    ['G', 'L', 'F', 'Q', 'S'],
    ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],
    ['Z', 'F', 'J'],
    ['D', 'L', 'V' , 'Z', 'R', 'H', 'Q'],
    ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D'],
  ]

  def __init__(self) -> None:
    # self.part_1()
    self.part_2()
  
  def part_1(self):
    with open('./input.txt') as file:
      for line in file:
        line = line.splitlines()[0]
        amount, origin, destination = self.parse_line(line=line)
        self.part_1_move_between_stacks(am=amount, ori=origin, dest=destination)

      self.find_top_crates()

  def part_1_move_between_stacks(self, am, ori, dest):
    for _ in range(am):
      if len(self.STACKS[ori]) <= 0:  # return if stack is empty
        return

      self.STACKS[dest].append(self.STACKS[ori].pop())

  def parse_line(self, line): 
        regex_match = re.match(r"^move (\d+) from (\d+) to (\d+)", line)  # use regex to match and parse numbers
        amount, origin, destination = regex_match.groups()  # separate numbers
        amount, origin, destination = int(amount), int(origin), int(destination)  # turn numbers into ints

        return amount, origin, destination
  
  def find_top_crates(self):
    top_of_stacks = []
    for stack in self.STACKS:
      if stack == None:
        continue

      top_of_stacks.append(stack[-1])
    
    print("".join(top_of_stacks))

  def part_2(self):
    with open('./input.txt') as file:
      for line in file:
        line = line.splitlines()[0]
        amount, origin, destination = self.parse_line(line=line)
        self.part_2_move_between_stacks(am=amount, ori=origin, dest=destination)
      
      self.find_top_crates()

  def part_2_move_between_stacks(self, am, ori, dest):
    self.STACKS[dest].extend(self.STACKS[ori][-am:])

    for _ in range(am):
      if len(self.STACKS[ori]) <= 0:
        return

      self.STACKS[ori].pop()
    


if __name__ == "__main__":
  Day5Attempt().part_2_move_between_stacks(am=2, ori=1, dest=2)
