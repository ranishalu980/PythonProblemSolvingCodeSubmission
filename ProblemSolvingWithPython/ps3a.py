# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 3A
# The PPS wordgame
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Jasdeep Singh <jasdeepcse@eternaluniversity.edu.in>
#
#

import random
import string
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # wordlist: list of strings
    # cite : https://stackoverflow.com/questions/17949508/python-read-all-text-file-lines-in-loop
    wordlist = []
    with open(WORDLIST_FILENAME) as f:
        for line in f:
            wordlist.append(line.strip().lower())
            if 'str' in line:
                break
            
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def getfrequencyDict(sequence):
                     
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordscore(word, n):
    
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """

    word_score = 0
    for letter in words:
        word_score += SCRABBLE_LETTER_VALUES[letter]

    word_score = word_score = len(word)
    if HAND_SIZE == len(word):
        word_score +=50
        
#
# Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in list(hand.keys()):
        for j in range(hand[letter]):
             print(letter, end=' ')              # print all on the same line
    print()                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    tem_hand = hand
    for letter in word:
        if hand[letter]>1:
            hand[letter]-= 1
        else:
            del(temp_hand[letter])

    return temp_hand

        
        
    

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    if word not in word_list:
        return False
        word_frequency = getfrequencyDict(word)
        for key_val in word_frequency:
            if key_val in word_frequency:
                return False
            elif word_frequency[key_val] >= hand[key_val]:
                return False

            return True
                
            
    
        return True
                                          
                

def calculateHandlen(hand):
    
   """Returns the length (number of letters) in the current hand.
      hand:dictonary(string>int)
      returns : integer
   """
   return sum(hand.values())

# Problem #4: Playing a hand

def playHand(hand, word_list,n):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n:integer(HAND_SIZE; i.e., hand size required for additional points)
      
    """
    #keep track of total score
    total_score = 0
    #as long as there  are still letters left in the hand:
    while calculateHandlen(hand)>0:
        #display the hand
        displayHand(hand)
        #Ask user for input
        user_input = input()
        #if the input i single period:
        if user_input == '.':
            #End the game (break out of the loop)
            break

        #otherwise(the input is not a singlr period):
        else:
            #if the word is not valid:
            if not isValidWord(user_input,hand,word_list):
                #Reject invalid word (print a messege followed by a blank line)
                print("Enter valid input.")
                print()
                #otherwise (the word is valid):
            else:
                    #Tell the user how many points  the word earned, and the updated total score,in one line followed by a blank line
                    word_score = getWordsscore(user_input,HAND_SIZE)
                    print(word_score)
                    total_score += word_score
                    print(total_score)
                    print()
                    #update the hand
        hand=updateHand(hand,user_input)


      #Game is over(user evtered a '.' or ran out of letters),so tell user the total score
    print(total_score)

                           
    # TO DO...

#
# Problem #5: Playing a game
def playGame(word_list):
    
    """
    Allow the user to play an arbitrary number of hands.
    
    1) Asks the user to input 'n' or 'r' or 'e'.
    
        * If the user inputs 'n', let the user play a new (random) hand.
        
        * If the user inputs 'r', let the user play the last hand again.
        
        * If the user inputs 'e', exit the game.
        
        * If the user inputs anything else, ask them again.
        
    2) When done playing the hand, repeat from step 1
    """
    # TO DO...
    user_hand = None
    while True:
        user_option = input("input n(new hand), or r(last hand) or e(exit)")
        if user_option == 'n':
            user_hand = dealHand
            playHand(user_hand,word_list,HAND_SIZE)
        elif user_option == 'r':
            playHand(user_hand,word_list,HAND_SIZE)
        elif user_option == 'e':
            return
        else:
            print("input is invalid.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = loadwords()
    playGame(word_list)
    print(dealHand(HAND_SIZE))

## it shows me that errorfunction' object has no attribute 'values'
    
