# Power of number
# How to calculate power of a number using recursion?

# 2 to the power of 3 = 8
# 8 = 1 x 2 x 2 x 2
# Hint: Integer to the power of Zero is equal to One
#   - Growth Rate Analogy - https://youtu.be/ntBWrcbAhaY?list=PLxvbXPxg6ydyg-x2_Dq_ZklZ_zMuTC_tq&t=44

def power_of_number(base, exp):

    # Constraint
    assert int(exp) == exp, 'Exponent must be a Integer'

    # Base Case - Return the Base itself when: Exponent equals One
    if (exp == 0):
        return 1
    elif (exp < 0):
        # Inductive Case: Negative Exponents
        return (1/base) * power_of_number(base, exp + 1)
    else:
        # Inductive Case: Positive Exponents
        return base * power_of_number(base, exp - 1)


print(power_of_number(2, +4))
print(power_of_number(2, -4))

# Negative Exponents - https://youtu.be/JnpqlXN9Whw
# Negative traditionally means the opposite | You can think of it as negation
