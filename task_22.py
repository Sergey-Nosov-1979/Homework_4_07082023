'''Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого 
множества. m — кол-во элементов второго множества. Затем 
пользователь вводит сами элементы множеств.'''

n = input("Введите число n элементов в списке №1: ")
n = int(n)
num_list_1 = []
for i in range(n):
    num = input("Введите i число списка №1 ")
    num = int(num)
    num_list_1.append(num)
print(num_list_1)
m = input("Введите число m элементов в списке №2: ")
m = int(m)
num_list_2 = []
for i in range(m):
    num = input("Введите i число списка №2 ")
    num = int(num)
    num_list_2.append(num)
print(num_list_2)
num_list3 = num_list_1+num_list_2
for i in set(num_list3):
    if num_list3.count(i) > 1:
        print(i)