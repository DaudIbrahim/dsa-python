# https://www.cuemath.com/numbers/hcf-highest-common-factor/
# Highest Common Factor (HCF, GCF, GCD) | https://www.calculatorsoup.com/calculators/math/gcf.php
# - HCF, GCF, GCD
# Find HCF by: Prime Factorization for (30, 42)

# Find HCF by: Euclid's Division Algorithm for (30, 42)
# Euclid's Algorithm: 42, 30, 12, 6, 0

def highest_common_factor(x, y):

    # Constraint
    assert int(x) == x and x >= 0, 'Numbers must be Positive Integers'
    assert int(y) == y and y >= 0, 'Numbers must be Positive Integers'

    large_number = x if x > y else y
    small_number = (x + y) - large_number
    [_, remainder] = divmod(large_number, small_number)

    # Base Case #0 - return when remainder is equal to one
    if (remainder == 0):
        return small_number
    elif (remainder == 1):
        return 1
    else:
        return highest_common_factor(small_number, remainder)


def least_common_multiple(x, y):
    # Khan Academy LCM lesson - https://youtu.be/znmPfDfsir8
    # LCM (x, y) =  (x * y) / HCF (x, y)
    # Use paper and a pencil to recollect how you arrived at this mathematical formula.

    hcf = highest_common_factor(x, y)
    [quotient, _] = divmod((x * y), hcf)
    return quotient


print('18, 12')
print(f'Higest Common Factor, {highest_common_factor(18, 12)}')
print(f'Least Common Multiple, {least_common_multiple(18, 12)}')
