import random

names_list = ['Вованчик', 'Светусик', 'Борюсик', 'Вероничка', 'Алиска', 'Сашенька', 'Антошка',
              'Ленусик', 'Викуся', 'Витенька', 'Владочка', 'Коленька', 'Егорка', 'Владюша',
              'Катенька', 'Андрюша', 'Алинка', 'Борюсик', 'Елизаветка', 'Анютка']

'''
Задание 1
Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N 
случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, 
рекомендуется использовать функцию random)
'''

def Get_random_names(names_list, N):
    random_names = random.choices(names_list, k=N)  # Методом выбираем из Списка имен N кол-во случайных имен
    return random_names  # Возвращаем сформированный список

'''
Задание 2
Напишите функцию вывода самого частого имени из списка на выходе функции F
'''

def Get_most_repeating(random_names_list): # Решение взято из ДЗ №3
    names_count = {}
    for i in range(len(random_names_list)): # Пробегаемся циклу по списку рандомных имен
        names_count[random_names_list[i]] = random_names_list.count(random_names_list[i]) # Создаем словать Имя:Повтор
    names_count = list(names_count.items()) # Преобразуем полученый Словарь в Список
    names_count.sort(key=lambda x: x[1], reverse=True) # Сортируем список по кол-ву повторений
    print(names_count[0]) # Выводим самый повторяющийся элемент


Get_most_repeating(Get_random_names(names_list, 100))

'''
Задание 3
Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F
'''
def Get_legendary_letter (random_names_list):


Get_most_repeating(Get_random_names(names_list, 100))
