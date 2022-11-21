# Jose Duran
# Program Status - Complete
# 
# Import distance.
import distance

# Define main function.
def main():
    # Display table format.
    print('Time \t Falling Distance')
    print()
    print('-----------------------------')
    print()
    # Generate for loop for time
    for time in range(1, 11):
        # Display time and the corresponding distance by calling to distance.py.
        print(time, '\t', \
              format(distance.falling_distance(time), '.2f'))

# Call back to main function.
main()
