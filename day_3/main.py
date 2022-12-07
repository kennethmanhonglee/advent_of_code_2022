from collections import Counter

class Day3Attempt():
  PART_1_PRIORITIES = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
  }

  def __init__(self) -> None:
    # self.part_1()
    self.part_2()

  def part_1(self) -> None:
    with open('./input.txt') as file:
      total_priority = 0
      for line in file:
        stripped_line = line.splitlines()[0]
        half_length = int(len(stripped_line) / 2)

        first_half, second_half = line[0:half_length + 1], line[half_length:]

        for char in line:
          if char in Counter(first_half) and char in Counter(second_half):
            repeated_item = char
            break
        
        total_priority += self.PART_1_PRIORITIES[repeated_item]
    
    print(total_priority)

  def part_2(self) -> None:
    with open('./input.txt') as file:
      group_member_count = 0
      counters = []
      total = 0

      for line in file:
        group_member_count += 1
        stripped_line = line.splitlines()[0]
        counters.append(Counter(stripped_line))

        if group_member_count == 3:
          for char in stripped_line:
            # if char in all 3 counters
            if all([char in ct for ct in counters]):
              total += self.PART_1_PRIORITIES[char]  
              break
          group_member_count = 0
          counters = []
      print(total)


if __name__ == "__main__":
  Day3Attempt()
