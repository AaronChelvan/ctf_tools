#!/usr/bin/python3
#A tool for encrypting messages with a rail fence cipher

print("What message do you want to encrypt?")
message = input()
print("How many rows do you want to use?")
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
	final_pattern.append(list(" " * len(message)))

i = 0
while i < len(message): #Add the message to the pattern to be printed
	j = i % gap_size
	if j <= gap_size/2:
		location = i % gap_size
	else:
		location = (gap_size - i) % gap_size
	final_pattern[location][i] = message[i]
	i += 1

for line in final_pattern: #Print out the pattern
	print("".join(line))

print() #Print a blank line

final_string = list(" "*len(message)) #Create a list containing all of the letters in the zig-zag pattern
counter = 0

for i in range(len(final_pattern)):
	for j in range(len(final_pattern[i])):
		if final_pattern[i][j] != " ":
			final_string[counter] = final_pattern[i][j]
			counter += 1
			
print("".join(final_string)) #Join the list to make a string, and print out the string
