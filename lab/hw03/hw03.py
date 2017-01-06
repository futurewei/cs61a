def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    minusOne,minusTwo,minusThree,k=0,0,0,0
    while True:
        if k==n and k<=3:
            return n
        elif k==n and k>3:
            return minusOne+2*minusTwo+3*minusThree
        else:
            if k<=3:
                minusThree=minusTwo
                minusTwo=minusOne
                minusOne=k
            else:
                temp=minusOne
                minusOne=minusOne+2*minusTwo+3*minusThree
                minusThree=minusTwo
                minusTwo=temp
            k=k+1

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    
    def changeDirection(k):
        if k%7==0 or has_seven(k):
             return True
        else:
             return False
    def helper(k,r,direction):
        if k==n:
            return r
        else:
            if changeDirection(k)==True and direction==0:
                return helper(k+1,r-1,1)
            elif changeDirection(k)==True and direction==1:
                return helper(k+1,r+1,0)
            elif changeDirection(k)==False and direction==0:
                return helper(k+1,r+1,0)
            elif changeDirection(k)==False and direction==1:
                return helper(k+1,r-1,1)
    return helper(1,1,0)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def power(amount):
        k=0
        while pow(2,k)<=amount:
            k=k+1
        return k-1
    def possible_way(amount, exponent):
        if amount<0:
            return 0
        elif amount==0:
            return 1
        if exponent<0 and amount>0:
            return 0
        return possible_way(amount-pow(2,exponent),exponent)+possible_way(amount, exponent-1)
    return possible_way(amount, power(amount))


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    def helper(n,start,mid,end):
        if n>0:
            helper(n-1,start,end,mid)
            print_move(start,end)
            helper(n-1,mid,start,end)
    return helper(n,start,2,end)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
