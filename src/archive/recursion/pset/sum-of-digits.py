# Sum of Digits
# How to find the sum of digits of a positive integer number using recursion ?

# 10 - 1 + 0 = 1
# 101 - 1 + 0 + 1 = 2
# 12345 - 1 + 2 + 3 + 4 + 5 = 15

def sum_of_digits(number):

    # Constraint
    assert int(
        number) == number and number >= 0, 'Number must be a positive integer'

    # Base Case - Quotient is less than < 10
    if (number < 10):
        return number
    else:
        # Inductive Case
        [quotient, remainder] = divmod(number, 10)
        return remainder + sum_of_digits(quotient)


print(sum_of_digits(10))
print(sum_of_digits(101))
print(sum_of_digits(12345))
