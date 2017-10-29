#!/usr/bin/envs python
# -*- encoding:utf-8

def cifra():
	alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	matrix = []

	for i in range(0, len(alfabeto) + 1):
		linha = []
		for j in range(0, len(alfabeto) + 1):
			if(i == 0 and j == 0):
				linha.append('#')
			elif(j == 0):
				linha.append(alfabeto[i - len(alfabeto) - 1])
			elif(i == 0):	
				linha.append(alfabeto[j - len(alfabeto) - 1])
			else:
				linha.append(alfabeto[j - len(alfabeto) - 2 + i])
		matrix.append(linha)		
	
	"""for i in range(0, len(alfabeto) + 1):
					print(matrix[i], end='')
					print("\n")"""
	
	return matrix		
	

def criptografar(frase, chave, matrix):
	
	for i in range(len(matrix)):	
		for j in range(len(matrix)):
			if(matrix[i][0] == frase):
				k = i
			if(matrix[0][j] == chave):
				w = j

	print(matrix[k][w], end='')

		

#def decriptogrgafar(frase, chave):


matrix = []
matrix = cifra()

key = []

chave = input("Informe a chave: ")
frase = input("Informe a frase: ")

chave = chave.upper().replace(" ","")
frase = frase.upper()

print("Chave: ",chave)
print("Frase: ",frase)

i = 0
j = 0
while (i < len(frase)):
	if(j == len(chave)):
		j = 0	
	key.append(chave[j])
	i+=1
	j+=1

print("Frase Criptografada")
for i in range(len(frase)):
	criptografar(frase[i], key[i], matrix)

print("\n")	