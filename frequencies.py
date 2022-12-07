"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for index in items:
        current_value = str(index)
        if current_value in frequencies:
            frequencies[current_value] +=1
        else:
            frequencies[current_value] =1
    return frequencies
