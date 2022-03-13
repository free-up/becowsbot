import random
print('Игрок называет числа.\nЕсли цифра угадана и стоит на нужном месте, это «бык».\nЕсли цифра угадана, но стоит не на своём месте, это – «корова».\n')
f = int(input("Сколько знаков будем угадывать? "))


n = list("0123456789")
random.shuffle(n)
a = ''.join([random.choice(n) for x in range(f)])
one_dig = []
for symbol in a:
    if '1234567890'.find(symbol) != -1:
        one_dig.append(int(symbol))

digits = []


step = int(0)
beef = int(0)
cow = int(0)

while one_dig != digits:
#	print(one_dig) #проверочный вывод
#	print(digits) #проверочный вывод
	digits = []
	b = input ("Введите число из " + str(f) + " знаков: \n")
		
#	print (len(b)) проверочный вывод
	while len(b) != f or b.isdigit() != True:
		b = input("Неверное количество знаков в числе. Число должно содержать только цифры. Введите " + str(f) + " цифр: \n")
	else:

		for symbol in b:
		    if '1234567890'.find(symbol) != -1:
		        digits.append(int(symbol))
		
		for i in range(f):
			if one_dig[i] == digits[i]:
	#			print ("Бык")
				beef += 1
			else:
				for j in range(f):
					if one_dig[i] == digits[j]:
	#					print ("Корова")
						cow += 1


	print("Быков: " + str(beef) + "; коров: " + str(cow))
	beef = 0
	cow = 0
	step +=1

print("Вы угадали за " + str(step) + " ходов!")

input() 

