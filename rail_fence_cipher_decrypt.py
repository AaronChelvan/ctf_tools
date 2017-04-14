#!/usr/bin/python3
#A tool to help decrypt rail fence cipher texts

print("What is the message you want to decrypt?")
message = input()
print("How many rows do you want to try?")
num_rows = int(input())

if num_rows <= 1:
	print("Input must be a positive integer greater than or equal to 2")
	exit()

gap_size = 2*num_rows - 2 #The number of spaces between characters in the top row + 1
			#The first number is always at position 0 
			#If gap_size = 7, the next number in the row will be at position 7
			#The number after that will be at position 14 etc...

final_pattern = [] #A 2D list containing the message put into a zig-zag pattern with the specified number of rows
for i in range(num_rows):
	final_pattern.append(list(" " * len(message))) #Fill up the 2D list with spaces

for i in range(len(message)): #Loop through final_pattern and place a '-' character in every position where a letter from the message should be
	j = i % gap_size
	if j <= gap_size/2:
		location = i % gap_size
	else:
		location = (gap_size - i) % gap_size
	final_pattern[location][i] = "-"
	i += 1

counter = 0
for i in range(len(final_pattern)): #Loop through final_pattern and replace all '-' characters with the letters from the message
	for j in range(len(final_pattern[i])):
		if final_pattern[i][j] == "-":
			final_pattern[i][j] = message[counter]
			counter += 1

for line in final_pattern: #Print out the pattern
	print("".join(line))

print() #Print a blank line

final_string = list(" "*len(message)) #Create a list containing all of the letters in the zig-zag pattern

for i in range(len(final_pattern)):
	for j in range(len(final_pattern[i])):
		if final_pattern[i][j] != " ":
			final_string[j] = final_pattern[i][j]
		
print("".join(final_string)) #Join the list to make a string, and print out the string
