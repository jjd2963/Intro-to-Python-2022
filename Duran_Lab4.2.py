# Jose Duran
# Program Status - Complete
# This program uses a loop to display a
# table of rise in ocean levels per year

# Print the table headings.
print('Year\tRise (in millimeters)')
print()
print('------------------------------------------')
print()

# Print the years and their rise in millimeters.
for year in range(1, 26):
    millimeters = year * 1.8
    print(year, '\t', format(millimeters, '.2f'))


