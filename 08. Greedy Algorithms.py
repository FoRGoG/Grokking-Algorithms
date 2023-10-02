from pprint import pprint

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']) # все станции
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])  # Айдахо, Невада, Юта
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None # Пока пустая
    states_covered = set()
    for station, states_for_station in stations.items(): # station - ключи, states_for_station - значения
        covered = states_needed & states_for_station # проверяем пересекающиеся варианты
        if len(covered) > len(states_covered): # если длина варианта больше предыдущего
            best_station = station # получаем новое название лучшей станции
            states_covered = covered # и получаем его штаты

    states_needed -= states_covered
    final_stations.add(best_station)
pprint(final_stations)

