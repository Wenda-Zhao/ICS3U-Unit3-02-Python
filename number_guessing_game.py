#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Nov 2020
# This program guessing number is 5


import constants


def main():
    # this function guessing number is 5

    # input
    your_number = int(input("Enter your number (between 0 and 9): "))
    print("")

    # process
    if your_number == constants.CORRECT_NUMBER:
        # output
        print("You are correct!")
    if your_number > constants.CORRECT_NUMBER:
        # output
        print("You are wrong...")
    if your_number < constants.CORRECT_NUMBER:
        # output
        print("You are wrong...")


if __name__ == "__main__":
    main()
