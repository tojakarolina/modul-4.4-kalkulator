import sys

def shopping(function, num_1, num_2):
    if function == 1:
            addiction = num_1 + num_2
            print(addiction)
    elif function == 2:
            subtraction = num_1 - num_2
            print(subtraction)
    elif function == 3:
            multiplication = num_1*num_2
            print(multiplication)
    elif function == 4:
            division = num_1 / num_2
            print(division)
    return function

if __name__ == "__main__":
    print(sys.argv[1:])
    shopping(1, 2, 3)
