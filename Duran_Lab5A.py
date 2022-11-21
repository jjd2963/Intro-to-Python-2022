# Jose Duran
# Program Status = Complete
# This program aks to input 5 judge scores and averages them
# To find how many stars you get.

# Definition of the main function.
def main():
    # Assign accumulator.
    total = 0.0
    # Assign a for loop to get the total of the 5 scores.
    for rating in range(5):
        score = int(input("Enter a judge's score from 0-10: "))
        while score < 0 or score > 10:
            print('ERROR: the score cannot be below 0 or above 10.')
            score = float(input("Enter a judge's score from 0-10: "))
        total += score
    # Average the scores.
    average = total / 5
    # Call to function that determines the number of stars.
    determine_stars(average)

# Definition of Determine Stars function.
def determine_stars(number):
    # Assign if-elif-else statement to determine number of stars.
    if number >= 9:
        print('Your score of', format(number, '.2f'), 'gives you *****')
    elif number >= 8:
        print('Your score of', format(number, '.2f'), 'gives you ****')
    elif number >= 7:
        print('Your score of', format(number, '.2f'), 'gives you ***')
    elif number >= 6:
        print('Your score of', format(number, '.2f'), 'gives you **')
    elif number >= 5:
        print('Your score of', format(number, '.2f'), 'gives you *')
    else:
        print('Your score of', format(number, '.2f'), \
              'gives you no stars. Do better!')
# Callback to main function.
main()

