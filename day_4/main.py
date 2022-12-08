class Day4Attempt():
  def __init__(self) -> None:
    self.part_1()
    self.part_2()

  def part_1(self):
    with open('./input.txt') as file:
        total = 0
        for line in file:
          first, second = line.splitlines()[0].split(',')  # remove \n, take string, and split into 2 lists

          # split each list into tuple of 2 nums - (A,B) (C,D)
          A, B = tuple(int(num) for num in first.split('-'))
          C, D = tuple(int(num) for num in second.split('-'))

          if (A <= C <= D <= B) or (C <= A <= B <= D):
            total += 1

        print(total)

  def part_2(self):
      with open('./input.txt') as file:
        total = 0
        for line in file:
          first, second = line.splitlines()[0].split(',')  # remove \n, take string, and split into 2 lists

          # split each list into tuple of 2 nums - (A,B) (C,D)
          A, B = tuple(int(num) for num in first.split('-'))
          C, D = tuple(int(num) for num in second.split('-'))

          if (A <= C <= B) or (A <= D <= B) or (C <= A <= D) or (C <= B <= D):
            total += 1

        print(total)

if __name__ == "__main__":
  Day4Attempt()
