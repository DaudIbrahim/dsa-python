def power_of_two(n):

    val = 1
    index = 0

    while (index < n):
        val = (val * 2)
        index += 1

    return val


print(power_of_two(5))
