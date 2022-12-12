class Day6Attempt():
  def __init__(self) -> None:
    self.part_1(distinct_num_count=4)  # part 1
    self.part_1(distinct_num_count=14)  # part 2

  def part_1(self, distinct_num_count: int):
    with open('./input.txt') as file:
      """
      use a sliding window

      4 chars
      if there are repeated chars within the 4 chars in the window:
          move the slower index / pointer + 1
      else return faster index
      """

      i, j = 0, distinct_num_count
      code = file.read()
      
      while j < len(code) - 1:
        if len(set(code[i:j])) == len(code[i:j]) == distinct_num_count:
          print(j)
          return j
        else:
          i += 1
          j += 1


      raise Exception("not found")


  def part_2(self):
    pass


if __name__ == "__main__":
  Day6Attempt()
