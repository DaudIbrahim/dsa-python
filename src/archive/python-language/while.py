number = 10

# A while Loop
while number < 10:
    print(f"Number is {number}!")
    number = number + 1

# Python does not have built-in functionality to explicitly create a do while loop like other languages. But it is possible to emulate a do while loop in Python.
# https://www.freecodecamp.org/news/python-do-while-loop-example/
# emulate a do while loop in Python
while (True):
    print(f"Number is {number}!")
    if (number >= 10):
        break
