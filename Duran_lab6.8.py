# This program reads the data in te random.numbers.txt file
# and displays the sum and number of lines.
def main():
    # Assign the accumulators.
    total = 0
    total_lines = 0

    # Open the random.numbers.txt file
    infile = open('random.numbers.txt', 'r')

    # Assign a loop that finds the sum.
    for line in infile:
        line.rstrip('\n')
        amount = int(line)
        total += amount
        total_lines += + 1

    # Find the average of the sum.
    average = total / total_lines
    
    # Close the file.
    infile.close()

    # Display the total, number of lines, and the average. 
    print('The total is: ', total)
    print('The total number of lines is: ', total_lines)
    print('The average is: ', format(average, '.2f'))
    
# Call the main function.
main()
