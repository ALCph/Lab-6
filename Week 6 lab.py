#1.)
# Opening the file
file = open('numbers.txt', "r")

# Displaying the file contents
for line in file:
	number = int(line)
	print(number)

#Close the program
file.close()
#----------------------------------------------------------

#2.)
# Getting user input
filename = input("Enter the name of the file to open: ")

#Opening the file to get the lines
file = open(filename, 'r')
lines = file.readlines()
#Printing the lines
for line in lines[:5]:
    print(line)
# Close the program
file.close()
#----------------------------------------------------------

#3.)
# The user input
filename = input("Enter the name of the file to open: ")

#Opening the file to get the lines
file = open(filename, 'r')
lines = file.readlines()
#Printing the lines
for i in range(len(lines)):
    i = int(i)
    print(f'{i + 1}: {lines[i].rstrip()}')
# Close the program
file.close()
#----------------------------------------------------------

#4.)
#Getting names
file = open('names.txt', 'r')
names = file.readlines()
#The name variable
name_count = 0

# Counting the number of names
for i in names:
    name_count += 1

file.close()
# printing the result
print(f"The number of names in names.txt is: {name_count}")
#----------------------------------------------------------

#5.)
# Very similar to problem #3 where we take the str and convert it to int
# Opening the file to get the lines
total = 0
file = open('numbers.txt', 'r')
numbers = file.readlines()
# Conversion of the str into i through the use of a for statement
for i in numbers:
    i = int(i)
    total += i
# The output
print(f' the sum of the numbers found in numbers.txt is: {total}')

