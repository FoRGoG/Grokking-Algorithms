from pprint import pprint


graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = None

processed = []



"""node = find_lowest_cost_node(costs) # Найти узел с наименьшей стоимостью среди необработанных
while node is not None: # Если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n] # Если к соседу можно быстрее
        if costs[n] > new_cost: # добраться через текущий узел...
            costs[n] = new_cost # ...обновить стоимость для этого узла
            parents[n] = node # Этот узел становится новым родителем для соседа
    processed.append(node) # Отмечаем узел, как отработанный
    node = find_lowest_cost_node(costs) # Находим следующий узел обработки и повторяем цикл"""


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs: # Перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # Если это узел с наим. стоимостью и еще не обратан...
            lowest_cost = cost # ...он назначается новым узлом с наим. стоимостью
            lowest_cost_node = node
    pprint(lowest_cost_node)

find_lowest_cost_node(costs)

