import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas!")

nrLetters = int(input("Quantas letras você gostaria na sua senha?\n"))
nrNumbers = int(input("Quantos números você gosataria na sua senha?\n"))
nrSymbols = int(input("Quantos símbolos você gostaria na sua senha?\n"))

lstPassword = []

for char in range(1,nrLetters + 1):
    lstPassword += random.choice(letters)
for char in range(1, nrNumbers + 1):
    lstPassword += random.choice(numbers)
for char in range(1, nrSymbols + 1):
    lstPassword += random.choice(symbols)

print(lstPassword)
random.shuffle(lstPassword)
print(lstPassword)

password = ""

for char in lstPassword:
    password += char

print(f"Sua senha é {password}")