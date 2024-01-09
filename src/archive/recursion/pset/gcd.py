
def gcd(x, y):

    # Constraint
    assert int(x) == x and int(y) == y, 'Numbers must be an Integer'

    if (x < 0):
        x = x * -1

    if (y < 0):
        y = y * -1

    # Base Case
    if (y == 0):
        return x
    else:
        # ------------- Remainder %
        return gcd(y, x % y)


print(f'GCD of 48 & 18 is {gcd(48, 18)}')
print(f'GCD of 18 & 48 is {gcd(18, 48)}')
print(f'GCD of 5 & 3 is {gcd(5, 3)}')
