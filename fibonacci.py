#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_number():
  #positive integer and validate input
    num = int(input("Enter how many terms of the Fibonacci sequence you want: "))
    while num <= 0:
        print("Please enter a positive integer.")
        num = int(input("Enter how many terms of the Fibonacci sequence you want: "))
    return num


def generate_fibonacci(n):
  #Generate Fibonacci sequence up to n terms and return list
  sequence = []
  a, b = 0, 1
  for i in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

def print_sequence(sequence):
  #print the Fibonacci sequence 
  print("Fibonacci Sequence:")
  for num in sequence:
    print(num, end=" ")
  print() #newline

n = get_number()
sequence = generate_fibonacci(n)
print_sequence(sequence)




