print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 > num2:
  max = num1
else:
  max = num2
if num3 > max:
  max = num3
print(f'Наибольшим числом из чисел {num1, num2, num3} является {max}')  
           
