#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

x = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(x), 2):# 1- индекс первого элемента, len(x)- показывает что идем до концв списка, 2- шаг
    sum += x[i]
print(f"{x} -> сумма элементов на нечетных позициях = {sum}")



