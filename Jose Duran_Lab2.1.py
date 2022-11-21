# Jose Duran
# Program Status = Complete
# This program gets the amount of servings desired and
# calculates the amoount of each ingredient needed for
# the desired servings.

# Get the amount of servings of spaghetti sauce wanted.
servings_wanted = float(input('Enter the number of servings of spaghetti ' \
                  'sauce you want to make: '))
# List the initial amount of servings of spaghetti sauce.
initial_servings = 4

# Assign the initial amounts of ingredients per the initial
# amoiunt of servings of spaghetti sauce.
initial_cups_tomato_sauce = 2
initial_cups_tomato_paste = .333
initial_cloves_garlic = 2
initial_tablespoons_oregano = 1

# Display text for ingredients needed
print('To make', servings_wanted,
      'servings of spaghetti sauce, you will need:')

# Calculate the final cups of tomato sauce for the amount of
# servings of spaghetti sauce wanted.
final_cups_tomato_sauce = servings_wanted * (initial_cups_tomato_sauce
                                             / initial_servings)

# Display the final cups of tomato sauce
print(format(final_cups_tomato_sauce, '.2f'),
      'cups of tomato sauce')

# Calculate the final cups of tomato paste for the amount of
# servings of spaghetti sauce wanted.
final_cups_tomato_paste = servings_wanted * (initial_cups_tomato_paste
                                             / initial_servings)

# Display the final cups of tomato paste
print(format(final_cups_tomato_paste, '.2f'),
      'cups of tomato paste')


# Calculate the amount of cloves of garlic for the amount
# of servings of spaghetti sauce wanted.
final_cloves_garlic = servings_wanted * (initial_cloves_garlic
                                         / initial_servings)

# Display the final cloves of garlic
print(format(final_cloves_garlic, '.2f'),
      'cloves of garlic')

# Calculate the amount of tablespoons of oregano for the 
# amount of servings of spaghetti sauce wanted.
final_tablespoons_oregano = servings_wanted * (initial_tablespoons_oregano
                                         / initial_servings)

# Display the final tablespoons of oregano
print(format(final_tablespoons_oregano, '.2f'),
      'tablespoons of oregano')

