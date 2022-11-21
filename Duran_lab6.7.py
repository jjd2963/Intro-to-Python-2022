# This program writes a series of random numbers
# Specified by the user.
# Import random.
import random
# Define the main function.
def main():
    try:
        # Open the random.numbers.txt file.
        numbers_file = open('random.numbers.txt', 'w')
        
        # Ask the user to input the amount of numbers.
        amount_number = int(input('Enter the amount of random numbers you want: '))

        # Assign a loop that generates random numbers.
        for number in range(1, amount_number + 1):
            number = random.randint(1, 500)
            # Write the numbers in the file
            numbers_file.write(str(number)+ '\n')

        # Close the files. 
        numbers_file.close()
        
    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')
        
# Call the main function.
main()
