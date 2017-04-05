"""
 Charlie Ang
 CSC 4800 Python Applications Programming
 Lab # 1
 Dr. Tindall
 January 9, 2017

 This program takes an input file with a collection of data values representing
 quiz scores and the number of students that received each score. The program
 will then store this data into a dataset collection. An analysis will then be
 completed to determine the lowest quiz score that any student received,
 the highest quiz score that any student received, and the largest frequency count for
 any of the quiz scores. A bar chart table and graph will also be outputted.
"""
import sys

MAX = 51                                        #max size of list. 0 - 50 for 51 possible quiz score values

def prompt():
    """
    This function outputs an introduction and prompts the user to enter an
    input filename. Returns the input file name that user provides
    """
    print('Welcome to the Quiz Score Frequency Analyzer, written by Charlie Ang')
    inputfilename = input('Enter the input data filename: ') # stores user input for filename in inputfilename
    print('Reading file ' + inputfilename + ' input:')
    return inputfilename


def lowestQuizScore(aList):
    """
    This function takes in a list of integers as a parameter. It then finds and returns
    the lowest quiz score (first element in list that is not equal to 0).
    :return:
    """
    i = 0
    freq = aList[i];
    while freq == 0:
        i += 1                                   # increment through list
        freq = aList[i]
    return i


def highestQuizScore(aList):
    """
    This function takes in a list of integers as a parameter. It then finds and returns
    the highest quiz score (first element in list starting at the end and decrementing
    until finding a quiz score that has a value other than 0).
    :param aList:
    :return:
    """
    i = MAX - 1                                 # start at end of list
    freq = aList[i]
    while freq == 0:
        i -= 1                                  # decrement
        freq = aList[i]
    return i


def largestFrequency(aList):
    """
    This function takes in a list of integers as a parameter. It then iterates and returns the
    largest frequency count.
    :param aList:
    :return:
    """
    max = 0
    for i in aList:                            # i is each quiz score frequency
        if i >= max:
            max = i
    return max


def tableOutput(aList, low, high):
    """
    This function takes in a list of integers, an integer for lowest quiz score, and integer for
    highest quiz score. It then outputs a readable bar chart in a table format.
    :param aList:
    :param low:
    :param high:
    :return:
    """
    print('')
    print('---Input Data---')
    print('Score: Frequency Bar Chart')
    print('')

    for i in range(low, high + 1):             # + 1 since end range is exclusive and we want to include the high
        print('{0:5d}:{1:6d}   '.format(i, aList[i]), end='')   # i is quiz score, aList[i] is freq
        for j in range(0, aList[i]):           # ranges from 0 to frequency count for number of *
            print('*', end='')
        print('')


def verticalBarChart(aList, low, high, freq):
    """
    This function takes in a list of integers, an integer for lowest quiz score, integer for
    highest quiz score, and an integer for the largest frequency. It then outputs a readable bar chart
    graph in a horizontal arrangement where the quiz score values appear across the page and the asterisks
    are displayed vertically.
    :param aList:
    :param low:
    :param high:
    :return:
    """
    print('')
    print('Frequency: Score Bar Chart')
    print('')

    for i in range(freq, 0, -1):                 # freq starting from highest to 1, decrementing
        print('{0}{1:4d}:'.format('    ^', i), end='')
        for j in range(low, high + 1):  # from lowest quiz score to highest quiz score
            if i <= aList[j]:                    # if frequency for this score is this high
                print('  *', end='')             # two spaces plus asterisk
            else:
                print('   ', end='')             # three spaces per number
        print('')

    # Prints axis
    print('---------:', end='')
    for i in range((high - low) + 1):
        print('--^', end='')
    print('')

    # Prints score numbers for axis
    print('    Score: ', end='')
    for i in range(low, high + 1):
        print('{0} '.format(i), end='')
    print('')


def main():
    """
    Calls function to prompt user to input data filename.
    Opens file to read in quiz score and frequency values and then saves values in list.
    Calls function to find and print lowest quiz score.
    Calls function to find and print highest quiz score.
    Calls function to find and print largest frequency count.
    Calls function to output horizontal table.
    Calls function to output vertical bar chart.
    :return:
    """

    inputfilename = prompt()                    # calls prompt function to prompt for user input

    try:
        file = open(inputfilename, 'r')         # open input filename in read-only format
    except IOError:                             # if file cannot be open or read, terminate file
        print('Error: can\'t find file or read data. Program terminating.')
        #prompt()                                # re-prompt user
        sys.exit()                             # terminate program

    myList = [0] * MAX                          # initializes list for all quiz scores with frequency of zero
    #print(myList)                              # outputting values in list for debugging purposes

    quizScore = 0                               # variable to keep track of quiz score
    frequency = 0                               # variable to keep track of frequency

    #file.readline()
    for line in file:
        print(line, end='')
        splitLine = line.split()                # list of all values in string
        quizScore = int(splitLine[0])           # assign first number as quiz score
        frequency = int(splitLine[1])           # assign second number as frequency for that quiz score
        myList[quizScore] += frequency          # adds frequency to associated quiz score

    print('')
    lowestScore = lowestQuizScore(myList)       # lowest quiz score variable
    print('The smallest score value is ', lowestScore)

    highestScore = highestQuizScore(myList)     # largest quiz score variable
    print('The largest score value is ', highestScore)

    largestFrequencyCount = largestFrequency(myList)
    print('The largest frequency count is ', largestFrequencyCount)

    # Outputting horizontal table
    tableOutput(myList,lowestScore, highestScore)

    # Outputting vertical bar chart
    verticalBarChart(myList, lowestScore, highestScore, largestFrequencyCount)

    file.close()                                # close file so later processes can access file


if __name__ == '__main__':
    main()