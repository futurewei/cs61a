"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    count,total=1,0
    element_one=False
    while count<=num_rolls:
        outcome=dice()
        count=count+1
        if outcome==1:
           element_one=True
        total=total+outcome
    if element_one==True:
        return 0
    return total

    # END Question 1
def free_bacon(opponent):
        return 1+max(opponent//10, opponent%10)

def is_prime(outcome):
    if outcome<=1:
        return False
    for x in range(2, outcome):
        if outcome%x==0:
            return False
    return True

def next_prime(outcome):
    nex_prime=outcome
    while True:
        nex_prime=nex_prime+1
        if is_prime(nex_prime):
            return nex_prime
    return False

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    turn_score=0
    if num_rolls==0:
        turn_score=free_bacon(opponent_score)
    else:
        turn_score=roll_dice(num_rolls,dice)
    if is_prime(turn_score):
        turn_score=next_prime(turn_score)
    return turn_score
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score+opponent_score)%7==0:
       return four_sided
    else:
       return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    score0,score1=score0%100,score1%100
    first_digitA, last_digitA=score0//10, score0%10
    first_digitB, last_digitB=score1//10, score1%10
    if first_digitA==last_digitB and first_digitB==last_digitA:
        return True
    else:
        return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 <goal and score1<goal:
       dice=select_dice(score0,score1)
       if who==0:
           num_rolls=strategy0(score0,score1)
           turn_score=take_turn(num_rolls, score1, dice)
           score0=score0+turn_score
           if turn_score==0:
              score1=score1+num_rolls
       elif who==1:
           num_rolls=strategy1(score1, score0)
           turn_score=take_turn(num_rolls, score0, dice)
           score1=score1+turn_score
           if turn_score==0:
              score0=score0+num_rolls
       if is_swap(score0, score1):
          score0,score1=score1,score0
       who=other(who)
    # END Question 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    
    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)  here it uses  make_test_dice
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice) it means each time throw 2 dices, dice outcome=3,1,5,6 
    5.5   this time use roll_dice function

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    def call(*args):
        count, total=1,0
        while count<=num_samples:
            total=total+fn(*args)
            count=count+1
        """if fn is winner function, then it takes two strategies in, output win=1 lose=0
            average=total win/ total games= win rate"""
        average=total/num_samples
        return average
    return call
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    largest, number=0,1
    for num_dice in range(1, 11):
        temp=make_averaged(roll_dice, num_samples)(num_dice, dice)
        if largest<temp:
           largest,number=temp,num_dice
    return number
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    """make_ave(winner)(strategy)(baseline)  one use strategy, one use baseline, see who wins. person A wins,
    total+0, person B wins, total+1  example 33/1000 for A means A lost 33 games. so win rate = 1-33/1000
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)
    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))
    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))
    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))
    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))
    if True:  # Change to True to test always_roll(4)
        print('always_roll(4) win rate:', average_win_rate(always_roll(4)))
    "*** You may add additional experiments as you wish ***"

# Strategies
def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    bacon=free_bacon(opponent_score)
    if is_prime(bacon):
       bacon=next_prime(bacon)
    if bacon>=margin:
         return 0
    else:
         return num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    improvement=free_bacon(opponent_score)
    if is_prime(improvement):
        improvement=next_prime(improvement)
    score=score+improvement
    if is_swap(score,opponent_score):
        if opponent_score>score:
            return 0
        else:
            return num_rolls
    else:
        return num_rolls    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
        
        When game just starts:
             throw 2 die. (if you do free bacon, since opponent's score is only 0, you can merely add up 1 point. If opponent scores 20 points,  then it's getting hard to catch up)
        
        While your score is lower than your opponent's score:
        1. If you throw 0 die, get free bacon, and get a higher score than your opponent, but then need to swap scores with your partner: 
        if your swapped score will be less than your opponent's new score, do not throw 0 die. Throw a different number of die. (After testing, 2 is a good try)
        
        2. If you throw 0 die, get free bacon, get a higher score than your opponent, and would result in a  score-swap with your partner:
           if your swapped score will be more than your opponent's new score, throw 0 die.
        
        3. If you throw 0 die, get free bacon, and would not lead to a score-swap with your opponent: 
            if you are really behind, say behind by 20, then first try if free bacon can get you at least 7 points to catch up, if not, return a higher number of die in order to score more. (it's risky because your turnscore may become 0 if any of the die is 1, but that's the only way to catch up scores)
            if you are less behind, you can try to see if free bacon can get you at least 6 points to catch up, if not return a higher number of
                die in attempt to score more. (Also risky try, thus we want to try Free_bacon way first, which is not a risky try)

        When your score is higher than your opponent's score:
        1. If you can throw 0 die, and free bacon can get you at least 8 points to maintain the lead, and not need to swap scores, return 0. 
           If free bacon cannot get you at least 8 points, then return 2. (After testing, we found that 2 is a good try)
        
        2. If you throw 0 die, get free bacon, but end up needing to swap scores; do not return 0.(you don't want to lose the lead). 
           Therefore, you would return a number other than 0. After testing, 5 is a good try, even though if any of the die is 1,
           your turnscore would be 0, and opponent would add points.
    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN Question 10
    def bacon(score, opponent_score):
        improvement=free_bacon(opponent_score)
        if is_prime(improvement):
            improvement=next_prime(improvement)
        score=score+improvement
        return score
    new_score=bacon(score,opponent_score)
    swap=is_swap(new_score,opponent_score)
    """when game just starts"""
    if score==0 and opponent_score==0:
        return 2
    if score<opponent_score:
        num_rolls=swap_strategy(score,opponent_score,4)
        """free bacon would lead ur score lower than opponent. so dont roll 0 dice."""
        if 0!=num_rolls and swap:
            return 5
        elif not swap:
            if opponent_score-score>=20:
                return bacon_strategy(score,opponent_score,7,4)
            else:
                return bacon_strategy(score,opponent_score,6,4)
        elif 0==num_rolls and swap:
            return 0
    else:
        if not swap:
            return bacon_strategy(score,opponent_score,8,2)
        else:
            return 5
# END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
                        
    args = parser.parse_args()
    
    if args.run_experiments:
        run_experiments()
