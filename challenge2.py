#Create a function tuple_of_squares that accepts an integer n as input. 
# The function should generate a tuple containing the squares of all numbers from 1 to n (inclusive).

# def tuple_of_squares(n):
#     myTuple = ()
#     for i in range(1, n + 1):
#         # comma is important, this is how to create a single-item tuple in Python.
#         myTuple += (i ** 2,) 
#     return myTuple

# another way to do it is using a generator expression inside the tuple() function
def tuple_of_squares(n):
    return tuple(i ** 2 for i in range(1, n + 1))

number = int(input("Enter a number: "))

print(f"The tuple of squares from 1 to {number} is: {tuple_of_squares(number)}")
