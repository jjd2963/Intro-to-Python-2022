# Jose Duran
# Program Status - Complete
# This program calculates the total discount in relation
# to the amount of packages purchased and displays it.

#Ask user to enter the number of packages
package = int(input("Enter the number of packages: "))

# List all named constants
package_price = 149
package_a = 150
package_b = 100
package_c = 50
package_d = 10

# Determine the discount value 
if package >= package_a:
    discount = 0.4
elif package >= package_b:
    discount = 0.3
elif package >= package_c:
    discount = 0.2
elif package >= package_d:
    discount = 0.1
else:
    discount = 0

# Calculate the total package amount and total discount amount
gross_package_price = package * package_price
discount_price = gross_package_price * discount
total_price = gross_package_price - discount_price

# Display the total and total discount amount
print('Your total amount is: $', \
             format(total_price, ',.2f'), sep='')
print('Your total discount is $', \
             format(discount_price, ',.2f'), sep='')
