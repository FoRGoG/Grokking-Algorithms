from collections import deque
from pprint import pprint

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def search(name):
    search_queue = deque() # Создание новой очереди
    search_queue += graph[name] # Все соседи добавляются в очередь поиска
    searched = [] # Массив используется для остлеживания уже проверенных людей
    while search_queue: # Пока очередь не пуста
        person = search_queue.popleft() # Из очереди извлекается человек
        if not person in searched: #Человек проверяется только в том случае, если не проверялся ранее
            if person_is_seller(person): # Проверяем является ли это продавец манго
                print(person + ' is a mango seller!') # Да, это он
            else:
                search_queue += graph[person] # Не является, добавляем его друзей в очередь для поиска
                searched.append(person) # Человек добавляется в список уже проверенных
    return False

"""Вариант проверки в учебнике"""
#def person_is_seller(name):
#    return name[-1] == 'm'

"""Еще один вариант проверки для примера"""
def person_is_seller(name):
    return 'o' in name

pprint(graph) # Выводим весь словарь
search('you')