"""
opponent: 
  A - rock - 1pt
  B - paper - 2pt
  C - scissor - 3pt
me:
  X - rock - 1pt
  Y - paper - 2pt
  Z - scissor - 3pt

round outcome:
  loss - 0
  draw - 3
  win - 6

score for each round = your move + round outcome
  ex: 
    A X - draw (3) + rock (1) = 4
"""

class Day2Attempt():
  MOVES_SCORES : dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3
  }

  WINS_AND_LOSSES: dict[str, dict[str, int]] = {
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

  def __init__(self) -> None:
    total_points = 0
    with open("./input.txt") as file:
      for line in file:
        opp_move, my_move = line.splitlines()[0].split(' ')  # get rid of \n, and split returned string into their move and my move
        total_points += self.calc_points(opp=opp_move, my=my_move)
    
    print(total_points)
  
  def calc_points(self, opp, my) -> int:
    return self.MOVES_SCORES[my] + self.WINS_AND_LOSSES[opp][my]


if __name__ == "__main__":
  Day2Attempt()