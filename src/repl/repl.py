while True:
    try:
        input = int(input("How many numbers do you want to add (1-10): "))
        if 1 <= input <= 10:
            break
        else:
            print("Number must be between 1 and 10.")
    except Exception:
        print("Input must be a valid integer.")

print(input)
