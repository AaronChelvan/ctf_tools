#!/usr/bin/python3
#This program calculates the frequency of each character in a given text file
#Can be useful for solving substitution ciphers, or for identifying transposition ciphers
#Make sure that the text file you want to analyse is in the same directory as this program

import re

print("What is the name of the text file you want to analyse?")
file_name = input()
print("File name: " + file_name)

print("Do you want to ignore non-alphabetic characters? (yes/no)")
decision = input()
if decision == "yes":
	ignore_non_alphabet = True
elif decision == "no":
	ignore_non_alphabet = False
else:
	print("Invalid input")
	exit()

with open(file_name) as f: #Open the file
	text_lines = f.readlines()
f.close()

num_occurrences = {} #A dict containing unique characters as the keys, and the number of occurences of those characters as the values

if ignore_non_alphabet == True: #If the user wants to ignore non-alphabetic characters, strip them out from text_lines
	edited_lines = []
	for line in text_lines:
		temp = re.sub("[^a-zA-Z]", "", line)
		temp = temp.upper() #Convert the entire line to uppercase to avoid case sensitivity
		edited_lines.append(temp)
	text_lines = edited_lines

for line in text_lines:
	for char in line: #Count the occurences of each character
		if char in num_occurrences:
			num_occurrences[char] += 1
		else:
			num_occurrences[char] = 1

total_chars = 0
for char in num_occurrences.keys(): #Count the total number of characters in the file
	total_chars += num_occurrences[char]
print("Total number of characters: " + str(total_chars))

num_occurrences_list = [] #A list of 2-item lists. Each 2-item list contains a unique character as the first item, and the number of occurences of that character as the second item

for char in num_occurrences.keys():
	num_occurrences_list.append([char, num_occurrences[char]])

#Sort num_occurrences_list by order of frequency
num_occurrences_list = sorted(num_occurrences_list, key=lambda char: char[1])
num_occurrences_list.reverse() #Reverse it so that the most frequent characters are at the front

for char in num_occurrences_list:
	print("Character: " + repr(char[0]) + "\t" + "Occurred: " + str(char[1]) + " times\t" + "Frequency: " + str((char[1]/total_chars)*100) + "%")
