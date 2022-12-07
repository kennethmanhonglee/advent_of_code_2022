class Day2Attempt():
  MOVES_SCORES_part_1 : dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3
  }

  WINS_AND_LOSSES_part_1: dict[str, dict[str, int]] = {
    "A": {  # rock
      "X": 3,
      "Y": 6,
      "Z": 0
    },
    "B": {  # paper
      "X": 0,
      "Y": 3,
      "Z": 6
    },
    "C": {  # scissor
      "X": 6,
      "Y": 0,
      "Z": 3
    },
  }

  RESULT_SCORES_part_2: dict[str, int] = {
    "X": 0,
    "Y": 3,
    "Z": 6
  }

  OPP_MOVE_TO_MY_MOVES_SCORE_part_2: dict[str, dict[str, int]] = {
    "A": {
      "X": 3,
      "Y": 1,
      "Z": 2
    },
    "B": {
      "X": 1,
      "Y": 2,
      "Z": 3
    },
    "C": {
      "X": 2,
      "Y": 3,
      "Z": 1
    },
  }

  def __init__(self) -> None:
    self.day_2_part_1()
    self.day_2_part_2()
    

  
  def calc_points_part_1(self, opp, my) -> int:
    return self.MOVES_SCORES_part_1[my] + self.WINS_AND_LOSSES_part_1[opp][my]

  def day_2_part_1(self):
    total_points = 0
    with open("./input.txt") as file:
      for line in file:
        opp_move, my_move = line.splitlines()[0].split(' ')  # get rid of \n, and split returned string into their move and my move
        total_points += self.calc_points_part_1(opp=opp_move, my=my_move)
    print(total_points)

  def calc_points_part_2(self, opp, res) -> int:
    return self.RESULT_SCORES_part_2[res] + self.OPP_MOVE_TO_MY_MOVES_SCORE_part_2[opp][res]

  def day_2_part_2(self):
    total_points = 0
    with open('./input.txt') as file:
      for line in file:
        opp_move, result = line.splitlines()[0].split(' ')
        total_points += self.calc_points_part_2(opp=opp_move, res=result)
    
    print(total_points)
        

if __name__ == "__main__":
  Day2Attempt()


  '''
  A Z - ROCK, win = 6(win) + 2(paper)
  A Y - ROCK, tie = 3(tie) + 1(rock)
  A Z
  A X
  C Z
  B X
  '''