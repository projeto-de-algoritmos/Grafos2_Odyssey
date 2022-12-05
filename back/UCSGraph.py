import numpy as np
inf = np.inf

graph=[['Kephallonia','Elis',33],
['Kephallonia','Achaia',39],
['Kephallonia','Phokis',6],
['Kephallonia','Megaris',7],
['Elis','Achaia',6],
['Elis','Arkadia',2],
['Achaia','Arkadia',8],
['Achaia','Korinthia',21],
['Arkadia','Messenia',3],
['Arkadia','Lakonia',4],
['Arkadia','Korinthia',12],
['Korinthia','Megaris',11],
['Korinthia','Argolis',2],
['Messenia','Lakonia',1],
['Messenia','Kythera Island',9],
['Argolis','Hydrea',1],
['Argolis','Seriphos',2],
['Argolis','Attika',4],
['Argolis','Lakonia',13],
['Lakonia','Hydrea',15],
['Lakonia','Melos',16],
['Hydrea','Seriphos',1],
['Hydrea','Melos',2],
['Seriphos','Melos',3],
['Seriphos','Keos',2],
['Megaris','Attika',7],
['Megaris','Boeotia',26],
['Attika','Boeotia',17],
['Attika','Euboea',2],
['Attika','Andros',3],
['Attika','Keos',2],
['Boeotia','Lokris',21],
['Boeotia','Phokis',24],
['Boeotia','Euboea',20],
['Phokis','Malis',1],
['Phokis','Lokris',2],
['Lokris','Malis',1],
['Lokris','Euboea',2],
['Euboea','Makedonia',4],
['Euboea','Lemnos',26],
['Euboea','Skyros',2],
['Malis','Makedonia',2],
['Makedonia','Thasos',2],
['Thasos','Lemnos',2],
['Thasos','Lesbos',4],
['Lemnos','Lesbos',2],
['Lemnos','Skyros',27],
['Lemnos','Chios',3],
['Skyros','Chios',33],
['Skyros','Andros',2],
['Chios','Samos',18],
['Andros','Samos',16],
['Andros','Keos',5],
['Andros','Delos',13],
['Andros','Mykonos',14],
['Keos','Delos',7],
['Keos','Paros',6],
['Delos','Mykonos',1],
['Delos','Paros',1],
['Delos','Naxos',1],
['Mykonos','Naxos',1],
['Mykonos','Paros',1],
['Paros','Naxos',1],
['Samos','Kos',3],
['Naxos','Kos',1],
['Paros','Thera',7],
['Melos','Thera',10],
['Thera','Anaphi',1],
['Thera','Messara',3],
['Anaphi','Messara',4],
['Kythera Island','Messara',9],
['Kos','Nisyros',2],
['Anaphi','Nisyros',1],
['Anaphi','Pephka',3],
['Nisyros','Pephka',4],
['Messara','Pephka',2]]

nodes = ['Kephallonia','Phokis','Malis','Lokris','Boeotia','Makedonia','Megaris','Attika','Korinthia','Achaia',
'Elis','Arkadia','Argolis','Lakonia','Messenia','Hydrea','Seriphos','Melos','Kythera Island','Messara',
'Pephka','Thera','Anaphi','Nisyros','Paros','Naxos','Kos','Keos','Andros','Samos','Delos','Mykonos','Skyros','Euboea',
'Chios','Lemnos','Lesbos','Thasos']

def UCS(graph, costs, frontier, visited, cur_node):
  if cur_node in frontier:
    frontier.remove(cur_node)
  visited.add(cur_node)
  for i in graph:
    print(cur_node, frontier)
    print(costs[i[0]], costs[i[1]], costs[i[0]]+i[2])
    if(i[0] == cur_node and costs[i[0]]+i[2] < costs[i[1]]):
      frontier.add(i[1])
      costs[i[1]] = costs[i[0]]+i[2]
      path[i[1]] = path[i[0]] + ' -> ' + i[1]
  costs[cur_node] = inf #retorna o valor do custo para infinito
  frontier_city = min(costs, key=costs.get)
  if frontier_city not in visited:
    UCS(graph, costs, frontier, visited, frontier_city)


''' Inicio do programa'''

costs = dict()
path = dict()

'''define todos os custos como infinito inicialmente'''
for i in nodes:
  costs[i] = inf
  path[i] = ' '
  
  
frontier = set()
visited = set()

'''Entra com o estado de início e o estado alvo para fazer a buca'''
start_node = 'Kephallonia'
frontier.add(start_node)
path[start_node] = start_node
costs[start_node] = 0
UCS(graph, costs, frontier, visited, start_node)
goal_node = 'Malis'
print("Path with least cost is: ",path[goal_node])