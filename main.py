"""
Orlando Marin
Project number 2

Given the attached file of the 50 states and capitals, Project 2 is to create 
a game that will help your user learn the capital name of each state (Phase 1) 
and build a quizlet to test the learning (Phase 2). The following is offered 
as a guide to help you develop your program. Verify your results at the end of 
each step.

1. Create your dictionary from the text file. DO NOT just type the state and 
city names to create your dictionary with an assignment statement.
a. Read each line of the text file as a string. Note that each data line is in
the format “city, state”. Each line is terminated with a ‘\n’ that needs
to be stripped. [hint: rstrip( ) ]
b. With the comma as separator, you have to find the position of the
comma and separate the string into city name and state name. [hint:
split( ) ]
c. Add each state-capital pair to your dictionary with the state as the key
and the capital as the value.

2. After your dictionary is set up, you are ready to create Phase 1 of your 
game, which is to help your user learn the capital of each state. Your program 
will ask the user to input a state, and using the dictionary, your program will
output the capital of that state. Your program will loop to allow user to have
as many tries as desired but will allow the user to opt out to enter Phase 2 of
the game.

3. From the dictionary, create a list of the keys (state names). [hint: keys( )
returns the keys as dict_keys type. Function list( ) will convert / cast them 
into a list.]

4. Phase 2 of the game is to build a quizlet to ask user to give the name of 
the capital for a randomly chosen state.
a. Generate a random number (1 to 50) to select a random state from
the list.
b. Prompt user to type in capital’s name for that state. Match user’s
input to see if the response is correct or incorrect.
c. Keep count for correct and incorrect responses
d. Repeat for a total of 5 tries. Display game result.
"""

import pydoc
import random
    

def main():
    """
    The main function to run the program.
    It initializes the game by creating the dictionary, running Phase 1,
    creating the list of states, and conducting Phase 2 quiz.
    """
    # create the dictionary with all of the states and capitals
    statesAndCapitals = createDictionary()
    
    # start phase one where a user can learn the states and capitals
    phaseOneLearn(statesAndCapitals)
    
    # take all of the states from the dictionary and make a list out of them
    statesList = createListOfKeys(statesAndCapitals)
    
    # start phase 2 where a user is quizzed on the state capitals
    phaseTwoQuizlet(statesAndCapitals, statesList)
    
    print("Thanks for playing!")
    return
    
    
def createDictionary():
    """
    Reads the state and capital information from a file and creates a dictionary
    where the state names are keys and the capital cities are values.
    The data is read from a text file in the format "city, state".
    
    Returns:
        dict: A dictionary with states as keys and their corresponding capitals as values.
    """
    # create an empty dictionary that will hold each state and it's corresponding
    # state capital
    statesAndCapitals = {}

    # open the file stateCapitals.txt
    infile = open("/Users/orlandomarin/Downloads/stateCapitals.txt", "r")

    # read the file's contents into the dictionary with the state as the key and
    # the capital as the value
    for line in infile:
        # remove the newline character from the end of each line in the text file
        fileLine = line.rstrip("\n")

        # split each line of the text file by the comma and space
        splitStateCapital = fileLine.split(", ")

        # assign the first index of the splitStateCapital list to the state
        # variable
        state = splitStateCapital[1]

        # assign the zero index of the splitStateCapital list to the capital
        # variable
        capital = splitStateCapital[0]

        # states will be the key of my dictionary and capital will be the
        # corresponding value
        statesAndCapitals[state] = capital

    # close the file
    infile.close()
        
    # return the list
    return statesAndCapitals

  
def phaseOneLearn(statesAndCapitals):
    """
    Allows the user to input a state name to learn its capital.
    The user can continue learning or opt to move on to Phase 2 (the quiz).
    
    Args:
        statesAndCapitals (dict): A dictionary with state names as keys and capitals as values.
    """
    
    optOut = 0
    
    while optOut != 1:
        userState = input("Input a state, and I will tell you the state capital: ").title()
        if userState in statesAndCapitals:
            print(f"The capital of {userState} is {statesAndCapitals[userState]}")
            print("Think you know all the state capitals?")
            optOut = int(input("Press 0 to continue learning, or press 1 to move onto the quiz: "))
        else:
            print("Looks like what you input wasn't a state. Try again: ")
    
    print("Moving onto Phase 2!")


def createListOfKeys(statesAndCapitals):
    """
    Creates a list of state names from the provided dictionary of states and capitals.
    
    Args:
        statesAndCapitals (dict): A dictionary with state names as keys and capitals as values.
        
    Returns:
        list: A list of state names.
    """
    statesDictionary = statesAndCapitals.keys()
    statesList = list(statesDictionary)
    return statesList

      
def phaseTwoQuizlet(statesAndCapitals, statesList):
    """
    Conducts a quiz where the user is asked to provide the capital for a randomly chosen state.
    Tracks correct and incorrect answers and displays the results after five attempts.
    
    Args:
        statesAndCapitals (dict): A dictionary with state names as keys and capitals as values.
        statesList (list): A list of state names for selecting random states.
    """
    tries = 0
    correctAnswers = 0
    wrongAnswers = 0
    
    while tries < 5:
        randomNum = random.randint(1, 50)
        stateQuiz = statesList[randomNum - 1]
        userQuizAnswer = input(f"What is the capital of {stateQuiz}? ").title()
        
        if userQuizAnswer == statesAndCapitals[stateQuiz]:
            print("Correct!")
            correctAnswers += 1
        else:
            print("Incorrect!")
            wrongAnswers += 1
        tries += 1
            
    print("Quiz complete! Here are the results.")
    print(f"{correctAnswers} out of 5 answers were correct")
    print(f"{wrongAnswers} out of 5 answers were incorrect")
    
    return
    
        
# Start the program
if __name__ == "__main__":
    main()

pydoc.writedoc("main")
        
        
        
    