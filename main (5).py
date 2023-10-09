class player:
  def play(self):
    print("The Player is Playing cricket.")
class batsman(player):
  def play(self):
    print("The Batsman is Batting.")
class bowler(player):
  def play(self):
    print("The Bowler is Bowling")
batsman=batsman()
bowler=bowler()
batsman.play()
bowler.play()