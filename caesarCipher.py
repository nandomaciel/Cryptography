#!/usr/bin/env python
# -*- encoding: utf-8 -*-

cipher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypted(key, word):
	c = []
	for i in word:
		if(i == " "):
			c.append(" ")
		else:
			for j in range(len(cipher)):
				if(i == cipher[j]):
					c.append(cipher[(j + key) % 26])
	return c

def decrypted(key, word):
	d = []
	for i in word:
		if(i == " "):
			d.append(" ")
		else:	
			for j in range(len(cipher)):
				if(i == cipher[j]):
					d.append(cipher[(j - key) % 26])
	return d

def string(word):
	e = ""
	for i in range(len(word)):
		e += word[i]
	return e
	
text = raw_input("Enter a phrase or word: ")
k = int(input("Enter the value of the kay: "))
n = int(input("1-Encrypt\n2-decrypt\n>>> "))

text = text.upper()

if(n == 1):
	c = string(encrypted(k, text))
	print("Encrypted text: ")
	print(c)
else:
	d = string(decrypted(k, text))	
	print("Decrypted text: ")
	print(d)

