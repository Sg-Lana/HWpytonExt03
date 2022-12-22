#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


from random import randint

number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9)) #создаем рандомный список из чисел от 0 до 9

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        if i != number:
            a = list[i] * list[number] #первый элемент [0] * на элемент последний (размер списка-1 как раз последний индекс)
            list2.append(a)
            i += 1 #прибаввляем счетчик +1 с начала и -1 с конца, это стр 18
      
print(list)
print(list2)



