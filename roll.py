import random
from random import randrange


# roll a "die" some number of times.

# roll - run it once and go into a loop

# roll 1 - produce a number 1-6 random and print it

# roll 2 - produce two numbers 1-6 and print them

# roll 3 - produce three numbers and print them.

def die_rolling():
    return random.randrange(1, 7)


def number_of_die():
    return int(input("Please enter number of die: "))


def one_die():
    result = die_rolling()
    print("Die number " + str(result))


def two_die():
    result = die_rolling(), die_rolling()
    print("Die numbers " + str(result))


def three_die():
    result = die_rolling(), die_rolling(), die_rolling()
    print("Die numbers " + str(result))


def play_again():
    question = input("Play again y or n?")
    if question == "y":
        play()
    elif question == "n":
        print("Thanks for playing")
    else:
        print("Invalid Choice")
        play_again()


def play():
    x = number_of_die()
    if x == 1:
        one_die()
    elif x == 2:
        two_die()
    elif x == 3:
        three_die()
    else:
        print('invalid choice')
        play()
    play_again()


play()


