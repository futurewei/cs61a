#############
# Iterators #
#############
# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.sta=start
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        val=self.start
        self.start+=1
        return val
    def __iter__(self):
        return IteratorRestart(self.sta, self.end)


# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, letter):
        self.start=0
        self.end=len(letter)-1
        self.letter=letter
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        val=self.start
        self.start+=1
        return self.letter[val]
    def __iter__(self):
        return self

##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n>=1:
        yield n
        if n==1:
            return 1
        elif n%2==0:
            n=int(n/2)
        else:
            n=int(n*3+1)


