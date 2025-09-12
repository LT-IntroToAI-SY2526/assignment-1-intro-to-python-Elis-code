
"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check and we'll be doing them in class.

Make sure to complete the a1.py problems which should be AI generated.
"""
import math
import runpy
from typing import List, TypeVar 


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.


    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if(n >= 0):
        return n
    elif (n < 0):
        return n * -1


def factorial(n: int) -> int:
    if (n < 0):
        return print("factorials can't be negitive")
    else:
        return math.factorial(n)
    


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    return lst[::2]


def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    count = 0
    for i in range (0, len(lst)):
        count += lst[i]
    return count

def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    count = sum_list(lst) / len(lst)
    return count


def median(lst: List[int]) -> float:
    if not lst:
        return None
    
    lst.sort
    i = len(lst)
    if(i % 2 == 1):
        med = lst[i // 2]
        return med
    else:
        med1 = lst[i // 2 - 1]
        med2 = lst[i // 2]
        return med1 + med2




def duck_duck_goose(lst: List[str]) -> List[str]:
    n = 0
    count = 0
    while len(lst) > 2:
        count += 1
        if count == 3:
            lst.pop(n)
            count = 0
            if n >= len(lst):
                n = 0
        else:
            n = (n + 1) % len(lst)
    return lst




# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")