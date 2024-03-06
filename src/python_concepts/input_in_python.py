# flake8: noqa
# IQVIA Assesment invloved taking input from User. Python/JS/C#

# input (): This function first takes the input from the user and converts it into a string.
# The type of the returned object always will be <class ‘str’>.
# It does not evaluate the expression it just returns the complete statement as String.
# https://www.geeksforgeeks.org/taking-input-in-python/

# Note all input is string similar to JS getItems from LocaleStorage
# Therefore, need to cast to desired format; mosttly int
# TODO - Learn to manipulate strings in Python & more about typcasting
while True:
    try:
        user_input = int(input("How many numbers do you want to add (1-10): "))
        if 1 <= user_input <= 10:
            break
        else:
            print("Number must be between 1 and 10.")
    except Exception:
        print("Input must be a valid integer.")

print("\n")
print("User Input")
print(user_input)
print("\n")
