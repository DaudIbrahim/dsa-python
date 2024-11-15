# flake8: noqa
# IQVIA Assessment involved taking input from User. Python/JS/C#

# input(): This function first takes the input from the user and converts it into a string.
# The type of the returned object always will be <class 'str'>.
# It does not evaluate the expression; it just returns the complete statement as a string.

# From string, as needed, we can cast to the desired format; for example, int().
# TODO: learn to manipulate strings in Python & more about typecasting aka type conversion.

# https://www.geeksforgeeks.org/taking-input-in-python/

# Basic User Input
def take_user_input_as_int():
    while True:
        try:
            user_input = int(input("How many numbers do you want to add (1-10): "))
            if user_input >= 1 and user_input <= 10:
                break
            else:
                print("Number must be between 1 and 10.")
        except:
            print("Input must be a valid integer.")

    print("\nBasic User Input")
    print(f"User input: {user_input}\n")


take_user_input_as_int()
