# Calculate Average Temperature
def calculate_average_temperature():
    my_list = []
    number_of_days = 0

    try:
        # input
        while True:
            inp = int(input("How many day's Temperature? (1-10) : "))

            if inp >= 1 and inp <= 10:
                break

        number_of_days += inp

        for i in range(number_of_days):
            inp = int(input("Temperature for Day " + str(i + 1) + " - "))
            my_list.append(inp)

        # calculation
        average = sum(my_list) / len(my_list)
        result = 0

        for i in range(len(my_list)):
            if my_list[i] > average:
                result += 1

        print(f"\nNumber of Days above average: {result}\n")

    except Exception as e:
        print("Error!")
        print(e)


calculate_average_temperature()
