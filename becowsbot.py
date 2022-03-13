import random
import telebot

bot = telebot.TeleBot("5229989034:AAHRwe9hWFDx17jXVi18U6TmGVcp22GHWNY", parse_mode=None)

#объявляем переменные, создаем списки
steps = 0
beef = 0
cow = 0


@bot.message_handler(commands=['start','becows'])

def send_welcome(message):
	bot.reply_to(message, "Игрок называет числа.\nЕсли цифра угадана и стоит на нужном месте, это «бык».\nЕсли цифра угадана, но стоит не на своём месте, это – «корова».\n\nСколько знаков будем угадывать?\n")
	f = message.text
	#загадываем число			
	one_dig = []
	n = list("0123456789")
	random.shuffle(n)
	a = ''.join([random.choice(n) for x in range(int(f))])
	for symbol in a:
		if '1234567890'.find(symbol) != -1:
			one_dig.append(int(symbol))
	digits = []	
	#Сравниваем загаданное с вводом
	
	while one_dig != digits:
		bot.reply_to(message, str(one_dig) + "one_dig") #проверочный вывод
		bot.reply_to(message, str(digits) + "digits") #проверочный вывод
		
		#def send_welcome(message):
		
		bot.reply_to(message, "Введите число из " + str(f) + " знаков: \n")
		b = message.text
		#def send_welcome(message):
		bot.reply_to(message, str(len(b)) + "знаки") #проверочный вывод
		#Проверка на вшивость введенного числа
		while len(b) != f or b.isdigit() != True:
			bot.reply_to(message, "Неверное количество знаков в числе. Число должно содержать только цифры. Введите " + str(f) + " цифр: \n")
			b = message.text
		else:
			for symbol in b:
			    if '1234567890'.find(symbol) != -1:
			        digits.append(int(symbol))
		#Подсчет быков				
			for i in range(f):
				if one_dig[i] == digits[i]:
			#		print ("Бык")
					beef += 1
		#Подсчет коров
				else:
					for j in range(f):
						if one_dig[i] == digits[j]:
				#			print ("Корова")
							cow += 1

	#Вывод подсказки
		bot.reply_to(message, "Быков: " + str(beef) + "; коров: " + str(cow))
		beef = 0
		cow = 0
		steps +=1


def echo_all(message):
		bot.reply_to(message, "Вы угадали за " + str(step) + " ходов!")

bot.infinity_polling() 

