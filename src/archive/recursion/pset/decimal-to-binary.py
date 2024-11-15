# Convert a number from Decimal to Binary
# https://www.rapidtables.com/convert/number/decimal-to-binary.html

def decimal_to_binary(num):

    # Constraint
    assert int(num) == num and num >= 0, 'Number must be a positive integer'

    # Base Case
    if num in [0, 1]:
        return str(num)

    else:
        # Inductive Case
        [quotient, remainder] = divmod(num, 2)
        return decimal_to_binary(quotient) + str(remainder)


print(decimal_to_binary(2))
print(decimal_to_binary(5))
print(decimal_to_binary(101))
print(decimal_to_binary(56))
