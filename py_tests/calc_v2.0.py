# Дебильный калькулятор v2.0

# В этой версии рассматривается "Работа с модулями"

from colorama import init
# from termcolor import colored
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Back.GREEN )

what = input( "Что делаем? (+, -, /, *): " )

print( Back.CYAN )

a = int( input("Введи первое число: ") )
b = int( input("Введи второе число: ") )

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print("Результат: " + str(c))
elif what == "/":
	c = a / b
	print("Результат: " + str(c))
elif what == "*":
	c = a * b
	print("Результат: " + str(c))
else:
	print("Выбрана неверная операция!")