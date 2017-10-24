#!/usr/bin/env python
# -*- encoding: utf-8 -*-

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def frequency(word):
	analysis = []
	total = 0
	latter = 0
	for i in range(len(alphabet)):
		if(i != " "):
			for j in range(len(word)):
				if(alphabet[i] == word[j]):
					total+=1
					latter+=1		
			analysis.append(latter)
			latter = 0
	return analysis, total

word = input("Enter a phrase or word: ")
word = word.upper()

a, total = frequency(word)			
print("\nTotal of latters: ", total)
for x in range(len(alphabet)):
	print(alphabet[x], ": ", format(a[x] * 100 / total,'.2f'),"%")