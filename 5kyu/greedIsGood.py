#Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point
#A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.


def score(dice):
    count1 = dice.count(1)
    count2 = dice.count(2)
    count3 = dice.count(3)
    count4 = dice.count(4)
    count5 = dice.count(5)
    count6 = dice.count(6)
    points = 0
    if count1 >= 3:
        points = points+ 1000 + (count1-3)*100 
    if count2 >= 3:
        points = points+200
    if count3 >= 3:
        points = points+300
    if count4 >= 3:
        points = points+400
    if count5 >= 3:
        points = points+500 +(count5-3)*50
    if count6 >= 3:
        points = points+600
    if count1 <3:
        points = points + count1*100
    if count5 <3:
        points = points + count5*50
    return points
