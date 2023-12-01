#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 30, 2023
# This program displays your grade in percent based off your level


def calc_mark(level):
    # use a match case to show what percentages the levels are represented by
    match level:
        case "4+":
            return 97
        case "4":
            return 90
        case "4-":
            return 83
        case "3+":
            return 78
        case "3":
            return 75
        case "3--":
            return 71
        case "2+":
            return 68
        case "2":
            return 65
        case "2-":
            return 61
        case "1+":
            return 58
        case "1":
            return 55
        case "1-":
            return 51
        case "R":
            return 25

        case _:
            # if the user enters an invalid number, return -1
            return -1


def main():
    # get user level
    print("This program displays your grade in percent based off your level.")
    user_level = str(input("Enter your level (ex. 3+): "))

    # set calculated_mark to calc_mark() and call the function
    calculated_mark = calc_mark(user_level)

    # if the user enters an invalid number, tell them to enter a valid level
    if calculated_mark == -1:
        print("Please enter a valid level.")
    else:
        # otherwise display user level
        print(calculated_mark)


if __name__ == "__main__":
    main()
