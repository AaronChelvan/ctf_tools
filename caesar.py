#!/usr/bin/python3

#Caesar Cipher Solver
#Run this program with the message you want to decipher as the argument(s)
#It will print out all possible deciphered messages

import sys

message = sys.argv[1:]

if len(sys.argv) == 1:
	print("USAGE: ./caesar.py ENCRYPTED MESSAGE")
	exit()

print("Offset Size | Message")

for offset in range(26):
	print(str(offset).center(12) + "| ", end='')
	for word in message:
		for letter in word:
			#check if the letter is uppercase
			isUppercase = False
			if letter >= 'A' and letter <= 'Z':
				isUppercase = True
			
			#if the character is not an alphabetic character, ignore it and print it as it is
			if not((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')):
				print(letter, end='')
				continue
			
			#apply the offset
			toPrint = ord(letter) + offset
			
			#if the offsetted letter overflows the alphabet, wrap it back around to the beginning
			if toPrint > ord('z'):
				toPrint -= 26
			elif isUppercase == True and toPrint > ord('Z'):
				toPrint -= 26
			print(chr(toPrint), end='')
		print(" ", end='') #print a space in between words
	print() #print a newline
