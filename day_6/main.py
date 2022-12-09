class Day6Attempt():
  def __init__(self) -> None:
    self.part_1()

  def part_1(self):
    with open('./input.txt') as file:
      code = file.read()
      cache = dict()
      count = 0

      for i, char in enumerate(code):
        if char not in cache:
          if count == 4:
            print(i)
            return

          cache[char] = count
          count += 1
      raise Exception("not found")


  def part_2(self):
    pass


if __name__ == "__main__":
  Day6Attempt()
