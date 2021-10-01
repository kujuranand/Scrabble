# print time taken
import time
# ask user to input a word within given time
from pytimedinput import timedInput
# check if user input is in english dictionary 
from spellchecker import SpellChecker

# scabble game
while True:
    # introduction
    print()
    print("Let's play Scrabble!")
    print("You have 15 seconds to enter a word.")
    print("The word must have at least 4 alphabets.")

    # start game
    while 1:
        # user input to start game
        s1 = input("Do you wish to continue? (y/n): ")
        # press "y" to start game 
        if s1 == "y":
            break
        # press "n" to exit game    
        if s1 == "n":
            print("See you next time.")
            exit()
        # press either "y" or "n"
        else:
            print("Press 'y' to continue or 'n' to exit.")

    # ask user to enter a word in 15 seconds
    # input should be a dictinary word
    # input should be at least 4 letters long
    # input should have alphabets only
    while 2:
        # time taken to enter a word
        start = time.time()
        t1 = time.time()
        # user input with timeout
        s2, timeOut = timedInput("\nEnter a word: ", timeOut = 15)  
        t2 =time.time()
        # total time taken
        total_time = t2 - t1
        
        # timeout notification
        if(timeOut):
            print("Sorry, time's up. Try again.")

        # user input should be a dictionary word
        spell = SpellChecker()
        isincorrect = False
        misspelled = spell.unknown([s2])
        for word in misspelled:
            isincorrect = True
        
        # not alphabet notification
        if not s2.isalpha():
            print("Please use only alphabets.")
        # word length notification
        elif not len(s2) >= 4:
            print("Too short. Try again.")
        # dictionary word notification
        elif isincorrect == True:
            print("Incorrect word. Try again.")
        # break while loop
        else:
            break

    # define score for each alphabet
    score = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, 
            "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
            "d": 2, "g": 2,
            "b": 3, "c": 3, "m": 3, "p": 3,
            "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
            "k": 5,
            "j": 8, "x": 8,
            "q": 10, "z": 10}  

    # scrabble score function
    def scrabble_score(word):
        # upper and lower case alphabets will have the same value
        word = word.lower()
        scrabbleScore = 0
        # adding the score of each alphabet in the user input
        for i in word:
            scrabbleScore += score[i]
        # return the addition result as the scrabble score
        return scrabbleScore

    # print the time taken and the scrabble score
    print("Time taken:", int(total_time), "second/s")
    print("Scrabble score:", scrabble_score(s2), "points")
    print("Good job!!!")

    # play again
    while 3:
        # user input to play again
        s3 = input("\nDo you wish to play again? (y/n): ")
        # press "y" to play again 
        if s3 == "y":
            break
        # press "n" to exit game    
        if s3 == "n":
            print("See you next time.")
            exit()
        # press either "y" or "n"
        else:
            print("Press 'y' to continue or 'n' to exit.")