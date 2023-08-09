'''Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого 
множества. m — кол-во элементов второго множества. Затем 
пользователь вводит сами элементы множеств.'''

n = input("Введите число n элементов в списке №1: ")
n = int(n)
number_list_1 = []
for i in range(n):
    number = input("Введите i число списка №1 ")
    number = int(number)
    number_list_1.append(number)
print(number_list_1)
m = input("Введите число m элементов в списке №2: ")
m = int(m)
number_list_2 = []
for i in range(m):
    number = input("Введите i число списка №2 ")
    number = int(number)
    number_list_2.append(number)
print(number_list_2)
number_list3 = number_list_1+number_list_2
for i in set(number_list3):
    if number_list3.count(i) > 1:
        print(i)