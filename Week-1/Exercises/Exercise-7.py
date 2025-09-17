"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

def Convert_sign(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 

    # If string s is - or + or =, the we're good
    if s == '-' :
        return -1
    if s == '+' :
        return 1
    if s == '=' :
        return 0
    
    # Otherwise, return -100 (means we're not good)
    return -100

def ask_integer(n):
    prompt = "is it " + str(n) + "? (using  \'+\', \'-\' or \'=\') : "
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    guess = Convert_sign(input(prompt)) # Ask the user for their guess
    while guess == -100: # Repeat until the user inputs a valid character
        print('Please, enter a n integer number')
        guess = Convert_sign(input(prompt)) 
    
    return guess

def dichotomie(g, d):
    if(g == d) :
        return g
    m = int((d - g - 1) / 2) #just a dichotomy
    m += g
    a = ask_integer(m)
    if not a :
        return m
    elif a > 0 :
        return dichotomie(m +1 , d)
    else :
        return dichotomie(g , m-1)




print("Please think about a number between 1 and 100")
print("You will need to answer with either the sign \'+\' if my guess is too high, \'-\' if my guess is too low or \'=\' if I'm correct")

a = dichotomie(1, 100)
print("the result is " + str(a))