def is_palindrome(inputString):
    pointerStart = 0
    pointerEnd = len(inputString) - 1

    while pointerStart < pointerEnd:
        if inputString[pointerStart] == inputString[pointerEnd]:
            pointerStart += 1
            pointerEnd -= 1
        else:
            return False

    return True
