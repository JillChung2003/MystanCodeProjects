"""
File: hangman.py
Name: Jill
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program plays a letter guessing game called hangman.
    User is shown a set of dashes that match a word
    and has to guess what these letters are to reveal the hidden word.
    User has N_TURNS chances to try and win the game.
    """
    lives = N_TURNS
    answer = random_word()
    strOnScreen = ""
    for i in range(len(answer)):
        strOnScreen += '-'
    print('The word looks like: ' + str(strOnScreen))
    print('You have 7 wrong guesses left. ')
    while True:
        input_ch = input('Your guess: ')
        if not input_ch.isalpha():
            print('Illegal format. ')
        elif len(input_ch) > 1:
            print('Illegal format. ')
        else:
            input_ch2 = input_ch.upper()
            if input_ch2 in answer:
                ans = ''
                for j in range(len(answer)):
                    alphabet = answer[j]
                    if alphabet == strOnScreen[j]:
                        ans += alphabet
                    else:
                        if alphabet != input_ch2:
                            ans += '-'
                        else:
                            ans += input_ch2
                strOnScreen = ans
                if strOnScreen == answer:
                    break
                else:
                    print('You are correct! ')
                    print('The word looks like: '+str(ans))
                    print('You have ' + str(lives) + ' wrong guesses left. ')
            else:

                print("There is no " + input_ch2 + " 's in the word. ")
                lives -= 1
                if lives == 0:
                    break
                else:
                    print('The word looks like: ' + str(strOnScreen))
                    print('You have ' + str(lives) + ' wrong guesses left. ')
    if lives == 0:
        print('You are completely hung :( ')
    else:
        print('You are correct! ')
        print('You win!')
    print('The answer is: '+str(answer))


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
