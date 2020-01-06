# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:06:22 2019

@author: JosephKR
"""

# monthly expenditure program
# totals my monthly expenses
#demonstrates the user input

print("\n\n===========================================================")
print(""" Please enter your daily expenses
So that you can understand your monthly
expenditure """)

rent = int(input("This month's rent: "))
bus_card = int(input("This month's bus_card: "))
food = int(input("This month's food shopping : "))
dining_out = int(input("This month's dinner_out: "))
gifts = int(input("This month's gifts: "))
school_fees = int(input("This month's school fees: "))

grand_total = rent + bus_card + food + dining_out + gifts + school_fees

print(grand_total)

input("\npress enter key to exit: ")

#demonstrates the if, elif, else condition
print("\n\n===========================================================")
password = input("please enter your fevourate password: ")
if password == "hannah":
  print("Access granted, welcome!")
elif password == "mariam":
  print("Access granted, you must be a VIP")
else:
  print("Access denied, try again!")
print("\n\nplease press enter to exit.")

#demonstrates a while loop
print("\n\n===========================================================")
dna = "ACTG"
count = 0
while count < 4:
  print(dna[count])
  count += 1
print("\n\nplease press enter to exit.")

#demonstrates treating values as a condition in python
print("\n\n===========================================================")
cost = int(input("how much does it cost? "))
if cost:
  print("The price reasonable, thank you!")
else:
  print("It is quite expensive though, thank you!")
    
print("\n\nplease press enter to exit.")

#demonstrates the break and continue statements in a while loop
print("\n\n===========================================================")
count = 0
while True:
  count += 1
  if count > 100:
    break
  if count == 50:
    continue
  print(count)

print("\n\nplease press enter to exit.")

#demonstrates the logical operators not, and, or
print("\n\n===========================================================")

dna = ""
while not dna:
  dna = input("Please enter 4 nucleotides in order ATCG: ")
if dna[0] == "A" and dna[1] == "T":
  print("These are nucleotides A and T")
elif dna[2] == "C" and dna[3] == "G":
  print("These are nucleotides C and G")
else:
  print("You are missing ATCG")
  
print("\n\nplease press enter to exit.")
      
#demonstrates guess number game program
print("\n\n===========================================================")
import random
print("Please guess a number between 1 and 50")
number = random.randint(1,50)
guess = int(input("Guess a number: "))
trials = 1
while guess != number:
      if guess > number:
          print("Too high......")
      else:
          print("Too low.......")
      
      guess = int(input("Guess a number: "))
      trials += 1
print("Congratulations!, you guessed it and it was: ", number)
print("You guessed in just only", trials, "tries\n")

print("\n\nplease press enter to exit.")

#demonstrates a program that simulates a fortune cookie
print("\n\n===========================================================")
import random
fortune = random.randint(1,5)
print("The unique fortune: ", fortune, "\n")
print("\n\nplease press enter to exit.")

#demonstrates a program that flips a coin 100 times and tells the number of 
#heads and tails
print("\n\n===========================================================")
heads = 0
tosses = 0
tails = 0
while tosses < 100:
    flip = random.randrange(2)
    if flip == 0:
        heads += 1
    else:
        tails += 1
    tosses += 1
    
print("The number of heads are ", heads, "and the number of tails are ", tails)

import random

num_heads = 0
num_tails = 0

num_tosses = 0

while num_tosses < 100:
    flip = random.randint(0, 1) # with each flip, you get 0 or 1
    if flip == 0:
        num_heads += 1  # count heads
    else:
        num_tails += 1  # count tails
    num_tosses += 1     # count tosses
        
print("number of heads: ", num_heads)
print("number of tails: ", num_tails)

#demonstrating a for loop in python 
word = input("please enter a word of your choice: ")
for letter in word:
    print(letter)

for i in range(10):
    print("\n\n", i)

#Demonstrates the laength of the DNA sequebnce  and number of GCs
print("\n\n===========================================================")
dna_sequence = input("please enter your sequence: ")
length_dna = len(dna_sequence)
print("The length of your sequence is ", length_dna, "bp")
count_of_G = 0
count_of_C = 0
count_of_AT = 0
for nucleotide in dna_sequence:
    if nucleotide == "G":
        count_of_G += 1
    elif nucleotide == "C":
        count_of_C += 1
    else:
        count_of_AT += 1
print("count_of_G is ", count_of_G)
print("count_of_C is ", count_of_C)

#demonstrates immutability of strings
print("\n\n===========================================================")
message = input("Please enter your message here: ")
new_message = ""
VOWELS = 'aeiou'
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
print(new_message)
        
#demonstrates the not operator 
messege = ""
if not messege:
    print("\nevaluated to true")
else:
    print("evaluated to false")
 
#How to create an empty tuple 
print("\n\n===========================================================")
shopping = ()

if not shopping:
    print("\nThis is an empty tuple")
else:
    print("This is not an empty tuple")
    
#How to create a tupple with sequence elements
shopping_list = ("sugar",
                  "chicken",
                  "bread",
                  "rice")
print("\n", shopping_list)

#To loop through the elements of a tuple
for item in shopping_list:
    print("\n", item)
print("There are ", len(shopping_list), "items")
    
#indexing tuples
# display one item through an index
index = int(input("\nEnter the index number for an item in shopping_list: "))
print("At index", index, "is",  shopping_list[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("shopping_list[", start, ":", finish, "] is", end=" ")
print(shopping_list[start:finish])
input("\nPress the enter key to continue.")

#concatenating tuples
new_shopping = ("tea",
                "banana")
shopping_list += new_shopping
print("\n", shopping_list)

#creating a jumblee game
print("\n\n===========================================================")
# Word Jumble
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
#import a random module
import random

#create a sequence of words to choose from
WORDS = ("Joseph", "Elin", "Lisa", "Faith", "Sonia")

#pick a word randomly from WORDS
word = random.choice(WORDS)

correct = word

jumble = ""

#setting up the loop

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
Welcome to Word Jumble!
Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")


print("\n\n===========================================================")
#demonstrates list manipulation
inventory = ["Hannah", "Jacob", "Gamdad", "Elly", "Elin"]
for name in inventory:
    print(name)
    
input("\nPress the enter key to continue.")

#get the length of a list
print("There are ", len(inventory), "items in the inventory")

input("\nPress the enter key to continue.")

# test for membership with in a list

if "Hannah" in inventory:
    print("The name already exists in the inventory")
    
# display one item through an index

index = int(input("\nEnter the index number of an item in the inventory: "))
print("The item at index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue.")

# concatenate two lists
chest = ["gold", "gems"]
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

# assign by index
print("Exchange Hannah for Sebastian.")
inventory[0] = "Sebastian"
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

# assign by slice
print("You use your gold and gems to buy an orb of future telling.")
inventory[3:5] = ["John"]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

# delete an element
del inventory[2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")

# delete a slice
print("Your crossbow and armor are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\n\nPress the enter key to exit.")

print("\n\n===========================================================")
#demonstrates list methods
scores = []
choice = None

while choice != 0:
    print(
    """
    0 - Exit
    1 - Show Scores
    2 - Add a Score
    3 - Delete a Score
    4 - Sort Scores 
    """
    )
    
    choice = input("Choice: ")
    if choice == "0":
        print("Goodbye")
    elif choice == "1":
        print("High Scores")
        for score in scores:
        print(score)
    elif choice == "2":
        score = int(input("Enter your highest score: "))
        scores.append(score)
    elif choice == "3":
        score = int(input("Enter which score to remove: "))
        if score in scores:
            scores.remove(score)
        else:
            print("\nscore is not in the list of scores")
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
input("\n\nPress the enter key to exit.")

print("\n\n===========================================================")
#demonstrates nested sequences
scores = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]
print(scores)
print(scores[2])
print(scores[2][0])

a_score = scores[0]
print(a_score)
print(a_score[0])

#demonstrates Unpacking a Sequence
name, score = ("Moe", 1000)
print(name, "->", score)

# High Scores 2.0
# Demonstrates nested sequences
scores = []
choice = None
while choice != "0":
    print(
        """
        High Scores 2.0
        0 - Quit
        1 - List Scores
        2 - Add a Score
        """
        )
    choice = input("Choice: ")
    print()
    # exit
    if choice == "0":
        print("Good-bye.")
    # display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # add a score
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # keep only top 5 scores
    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")


# Demonstrates using dictionaries

sequences = {
        "V20-01-01" : "ACTGACTGCTGACTCGTAGC",
        "V20-01-02" : "CTGACGTCAGTCGACGGTAG",
        "V20-01-03" : "AGCTGCGTAGCGGTCCGTAG",
        "V20-01-04" : "ACTGACGTCCTGCGTGGGTC"
        }

#Using a Key to Retrieve a Value    
sequences["V20-01-01"]

#Testing for a Key with the in Operator Before Retrieving a Value
if "V20-01-04" in sequences:
    print("I know what V20-01-04  is. ")
else:
    print("I have no idea what V20-01-04 is. ")

#Using the get() Method to Retrieve a Value


#Demonstrates functions in python

# Demonstrates using functions

dna = input("please enter a DNA sequence: ")

#funtion definition
def GC_content (dna):
    """calculates the percentage of GC in a DNA sequence."""
    
    GC = float((dna.count("G") + dna.count("C")) / len(dna) * 100)
    return GC
    

#main
GC_percentage = GC_content(dna)
print(GC_percentage)


def instructions():
    """Display game instructions."""
    print(
        """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.
        You will make your move known by entering a number, 0 - 8. The number
        will correspond to the board position as illustrated:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        Prepare yourself, human. The ultimate battle is about to begin. \n
        """
        )
        
# main
print("Here are the instructions to the Tic-Tac-Toe game:")
instructions()

input("\n\nPress the enter key to exit.")

# Receive and Return
# Demonstrates parameters and return values
def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

# main
display("Here's a message for you.\n")
number = give_me_five()
print("Here's what I got from give_me_five():", number)
answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)
input("\n\nPress the enter key to exit.")

