
print("Welcome to the Magic Square!")

print('Enter in the magic square size you would like:')
size = int(input()) #Turns users number to an integer and stores it in variable size.

while size <= 0: #If the user does not enter a size greater than or equal to zero, they are asked to enter a new value.
    print('Please enter in a number that is greater than 0')
    print('Enter in the magic square size you would like:')
    size = int(input())

magic_sum = 0 #Initializes varialbe magic_sum
count = 1 #Initializes variable count starting at 1
#For loop adds together all value from 1 to size squared. Ex: If size is 3, 1 + 2 +...+ 9 = 45
for i in range(size ** 2):
    magic_sum += count 
    count += 1

magic_number = int(magic_sum / size) #Calculates magic_number and turns the float into an integer

print(f'The magic number for size {size} is {magic_number}.')

print('Enter in the values separated by spaces: ')

str_vals = input().split() #User inputs values seperated by spaces, splits values into a list of those vals. Each value is a string.
int_vals = [int(n) for n in str_vals] #Turns each value in str_vals to an integer. Eliminates leading zero/decimal places. Allows values to act as operands.
new_str_vals = [str(n) for n in int_vals] #Turns the values in int_vals back to a string, now without any possible leading zeros that the user entered.

int_vals_copy = int_vals[:] #Creates a copy of the list of integer values.
int_vals_copy.sort() #Sorts the list of integer values in ascending order.

index = 0 #Initializes index variable.
input_square = [['*' for i in range(size)] for j in range(size)] #Initializes 2D list for user's square.

print('Your square:')
"""
Nested for loop increments index variable and replaces each element in input_square with new_str_vals[index]. 
Prints list at index i joined at the end of each iteration to display the user's square.
"""
for i in range(size):
    for j in range(size):
        input_square[i][j] = new_str_vals[index]
        index += 1
    print(' '.join(input_square[i]))

expected_vals = [] #Initializes empty list expected_vals.

#For loop appends expected_vals with values from 1 to size squared
for i in range(size ** 2):
    expected_vals.append(i + 1)

'''
For loop checks to see if each value in expected_vals and int_vals_copy match.
If one of the values does not match, the user is notified and the loop is broken.
'''
for i in range(len(expected_vals)):
    if expected_vals[i] != int_vals_copy[i]:
        print(f'The input cannot be a magic square! There must be one of each value from 1 to {size**2}.')
        break

int_input_square = [['*' for i in range(size)] for j in range(size)] #Initializes a 2D list int_input_square

#For loop turns all elements in input_square to integers and adds them to list int_input_square
for i in range(size):
    for j in range(size):
        int_input_square[i][j] = int(input_square[i][j])

magic = True #Initializes magic Boolean to true

'''
For loop that sums each list at index i and, if the sum does not equal the magic number,
the magic Boolean is set to False and the user is notified that row i does not work.
'''
for i in range(size):
    if sum(int_input_square[i]) != magic_number:
        magic = False
        row = i
        print(f'Row {row} does not work! These are the values in row {row}: ', end = '')
        print(' '.join(input_square[i]))

total = 0 #Initializes total variable

'''
For loop that iterates through the i elements of the nested lists, summing the j elements of those nested lists and assigning each value to total.
If total does not equal magic_number, magic Boolean is set to False, and the user is notified that column i does not work. total is reset to 0.
'''
for i in range(size):
    for j in range(size):
        total += int_input_square[j][i]
    if total != magic_number:
        magic = False
        column = i
        print(f'Column {column} does not work! These are the values in column {column}: ', end = '')
        for k in range(size):
            print(f"{int_input_square[k][i]} ", end='')
        print()
    total = 0

'''
For loop that iterates through i lists, assigning the sum of the i elements to variable total.
If total does not equal magic_number, magic Boolean is set to False and the user is notified that Diagonal 1 does not work. Total is reset to 0.
'''
for i in range(size):
    total += int_input_square[i][i]
if total != magic_number:
    magic = False
    print('Diagonal 1 does not work! ')
    print('These are the values in diagonal 1: ', end = '')
    for i in range(size):
        print(f"{int_input_square[i][i]} ", end='')
print()
total = 0

'''
For loop that iterates through i lists, assigning the sum of the [(size - 1) - i] elements to variable total.
If total does not equal magic_number, magic Boolean is set to False and the user is notified that Diagonal 2 does not work.
'''
for i in range(size):
    total += int_input_square[i][(size - 1) - i]
if total != magic_number:
    magic = False
    print('Diagonal 2 does not work! ')
    print('These are the values in diagonal 2: ', end = '')
    for i in range(size):
        print(f"{int_input_square[i][(size - 1) - i]} ", end='')
print()

#If-else statement informs the user that their square is magic if magic is True, and not magic if False.
if magic:
    print('This is a magic square!')
else:
    print('This is not a magic square!')
