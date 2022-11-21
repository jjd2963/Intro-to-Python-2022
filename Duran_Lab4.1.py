#Jose Duran
# Program Status = Complete
# This program asks the user to enter their budget and
# runs a loop to determine if the amount spent is
# over or under their budget.

# Ask user to enter budget and amount.
budget = int(input('Enter amount budgeted for this month: '))
amount = int(input('Enter an amount spent (0 to quit): '))

# Assign an accumulator.
total = 0

# Assign a while loop that sums up each entered amount.
while amount != 0:
    total += amount
    amount = float(input('Enter an amount spent (0 to quit): '))

# Calculate over and under budget amounts.
over_budget = total - budget
under_budget = budget - total

# Display budget and amount spent.
print('Budgeted: $', format(budget, ',.2f'), sep='')
print('Spent: $', format(total, ',.2f'), sep='')

# Determine if over or under budget through 
# if-else statement, display the amount for either.
if total > budget:
    print('You are $', \
          format(over_budget, ',.2f'), \
          ' over budget. PLAN BETTER NEXT TIME!', sep='')
elif total == budget:
    print('You are just in your budget.')
else:
    print('You are $', \
          format(under_budget, ',.2f'), \
          ' under budget. GOOD JOB!', sep='')
