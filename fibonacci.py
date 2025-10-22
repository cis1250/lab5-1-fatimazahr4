#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_number():
  #positive integer and validate input
  while True:
  try:
    num = int(input("Enter how many terms of the Fibonacci sequence you want: "))
    if num <= 0:
      print("Please enter a positive integer.")
    else:
      return num
  except ValueError:
    print("Invalid input. Please enter an integer.")


def generate_fibonacci(n):
  #Generate Fibonacci sequence up to n terms and return list
  sequence = []
  a, b = 0, 1
  for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

def print_sequence(sequence):
  #print the Fibonacci sequence 
  print("Fibonacci Sequence:")
  for num in sequence:
    print(num, end=" ")
    print()  # for new line

