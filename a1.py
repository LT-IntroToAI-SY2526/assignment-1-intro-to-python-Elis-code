# Assignment 1: AI-Generated Python Problems
# Name: Eli Curran

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I a highschooler learning to code in python. I already know how to use java and C++. 
can you give me 5 practice problems to learn the basics of python syntax and any python only methods. 

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
Problem 1: Word Frequency Counter

Topic: Dictionaries, Loops, split(), String Methods

Write a Python function that takes a string of text and returns a dictionary with the frequency of each word. 
"""
import string
def word_frequency(text):
    # Removes punctuation using str.translate and finds the punctuatioing using .puncuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    # uses split() to split up each word ... duh
    words = text.split()
    
    freq = {}
    # creates an emty list to fill
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
    # for each word in words add the word to the list and add 1 to the count



"""
Problem 2: List Comprehension Filter

Topic: List Comprehensions

Write a function that takes a list of integers and returns a new list containing only the squares of even numbers.
"""
def squares_of_evens(nums):
    return [x**2 for x in nums if x % 2 == 0]
# if the number is even the number is taken squared and returned, goes throught the whole thing of numbers 


"""
Problem 3: Unique Elements with Sets

Topic: Sets, set(), len()

Write a function that takes a list and returns True if all elements are unique, otherwise False.
"""
def all_unique(lst):
    return len(lst) == len(set(lst))
# if the length of the origial list is equal to the list with all unique elements
"""
Problem 4: FizzBuzz with List Comprehension

Topic: Ranges, Conditionals, List Comprehension

Write a one-liner list comprehension to generate the classic FizzBuzz from 1 to 30.

For multiples of 3, use "Fizz"

For multiples of 5, use "Buzz"

For multiples of both, use "FizzBuzz"

Otherwise, use the number itself

Python Feature: One-liner with list comprehension and ternary expressions:
"""
def fizzbuzz(n):
    return ['FizzBuzz' if i % 15 == 0 else
            'Fizz' if i % 3 == 0 else
            'Buzz' if i % 5 == 0 else i
            for i in range(0, n)]
# takes in a number and iterates through it in a list
# checks to see if every number is divisable by 3 and 5
# also checks to see if it is divisable by the gcf of 3 and 5, returns priority
#if the number checked is not divisable by any it simply adds the number to the list

"""
Problem 5: File Word Count

Topic: File I/O, with, open(), read()

Write a Python function that takes a file name, reads the file, and returns the number of words.
"""
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)










# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
t = 'Hello world! Hello Python.'
assert word_frequency(t) == {'hello': 2, 'world': 1, 'python': 1}


print("\nTesting Problem 2:")
num = [1, 2, 3, 4, 5, 6]
assert squares_of_evens(num) == [4, 16, 36]

print("\nTesting Problem 3:")
set1 = [1, 2, 3, 4, 5]
set2 = [1, 2, 3, 3, 4]
assert all_unique(set1) == True
assert all_unique(set2) == False


print("\nTesting Problem 4:")
print(fizzbuzz(30)) 

print("\nTesting Problem 5:")



