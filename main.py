#  Задание 1:
n_task_1 = input(f'Введите {5} чисел:').split(' ')

new_list_task_1 = list(n_task_1)[:5]

print(new_list_task_1)

#  Задание 2:
a = [1, 2, 3, 4, 5]

del a[len(a) - 1]

print(a)

# Задание 3:
new_list_task_3 = list(input('Введите 10 чисел:').split(' '))

n_task_3 = input('Введите число:')

repetition_n_task_3 = new_list_task_3.count(n_task_3)

print('Число повторений:', repetition_n_task_3)

# Задание 4:
n_task_4 = int(input('Введите число:'))

new_list_task_4 = list(input(f'Введите {n_task_4} чисел:').split(' '))[:n_task_4]

new_list_task_4.reverse()

print(new_list_task_4)

# Задание 5:
new_list_task_5 = list(map(int, input(f'Введите {5} чисел:').split(' ')))[:5]
answer = []
for x in new_list_task_5:
    if x > 5:
        answer.append(x)
print(answer)

# Задание 6:
n_task_6 = int(input('Введите число:'))

new_list_task_6 = list(map(int, input(f'Введите {n_task_6} целых чисел:').split(' ')))[:n_task_6]
i = 1
max_list = new_list_task_6[0]
min_list = new_list_task_6[0]
while i < len(new_list_task_6):
    for x in new_list_task_6:
        if new_list_task_6[i] > new_list_task_6[i - 1]:
            max_list = new_list_task_6[i]
        if new_list_task_6[i] < new_list_task_6[i - 1]:
            min_list = new_list_task_6[i]
    i += 1
print('Максимальное число равно ', max_list)
print('Минимальное число равно ', min_list)

# Задание 7:
n_task_7 = int(input('Введите текст:'))
new_list_task_7 = 'Lorem 222 ipsum, 1234 dolor 1 sit amet'

digit_counter = 0
for i in new_list_task_7:
    if i.isdigit():
        digit_counter += 1
print(digit_counter)
