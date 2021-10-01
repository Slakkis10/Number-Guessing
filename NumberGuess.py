# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:08:48 2021

@author: Joela

This script is the Number Guesser. The user will guess a random number between,
and including, 1 and 100 until they guess the correct number
"""
    
# initialize
correct = False
minVal = 1;
maxVal = 100;
snarkyRemarks = ['HAHAHA stupid!', 'Dummy Butthole Face...',
                 'Did you just roll in from stupid town?!', 'Might as well call you Mojay LOL']

# Import modules
from random import randint

# InputCheck Definition
def InputCheck(answer):
    if answer.isnumeric() == False:
        raise TypeError()
    elif int(answer) < minVal or int(answer) > maxVal:
        raise ValueError()

# # Multiple Definition
# def Multiple(numGuess, answer):
    
# # Division Definition
# def Division(numGuess, answer):

# Main Script
numGuess = randint(minVal,maxVal)   #Generate random number for user to guess
answer = input('Guess a number between ' + str(minVal) + ' and ' + str(maxVal) + ': ')    #Get user input

while answer != numGuess:
    try:
        InputCheck(answer)           
        if int(answer) > numGuess:
            # Choose a snarky remark
            remarkIdx = randint(0, len(snarkyRemarks)-1)
            remark = snarkyRemarks[remarkIdx]
            
            # Let em know they is wrong
            print(remark + ' Your answer is too high. Guess again idiot.')
            
        elif int(answer) < numGuess:
            # Choose a snarky remark
            remarkIdx = randint(0, len(snarkyRemarks)-1)
            remark = snarkyRemarks[remarkIdx]
            
            # Let em know they is wrong
            print(remark + ' Your answer is too low. Guess again idiot.')
            
        else:
            correct = True
            print('WOW! You are so goddamn smart. Honestly, you should apply for Harvard.')
            break
                    
    except TypeError:
        print('"' + str(answer) + '" is an invlaid input stupid face! Please enter a numeric value between 1 and 100')
        
    except ValueError:
        print(str(answer) + ' is outside of the range of ' + str(minVal) + ' and ' + str(maxVal) + '. Please enter a numeric value between 1 and 100 moron')
    
    finally:
        if correct == False:
            answer = input('Guess a number between ' + str(minVal) + ' and ' + str(maxVal) + ': ')    #Get user input
        else:
            break     