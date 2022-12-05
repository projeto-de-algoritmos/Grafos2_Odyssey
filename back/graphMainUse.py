from graph import Graph, Node
from ucs_algorithm import UCS

def cityGraphUCS(begin, destiny):
  # Create graph
  G = Graph()

  G.add_node(Node('Kephallonia'))
  G.add_node(Node('Phokis'))
  G.add_node(Node('Malis'))
  G.add_node(Node('Lokris'))
  G.add_node(Node('Boeotia'))
  G.add_node(Node('Makedonia'))
  G.add_node(Node('Megaris'))
  G.add_node(Node('Attika'))
  G.add_node(Node('Korinthia'))
  G.add_node(Node('Achaia'))
  G.add_node(Node('Elis'))
  G.add_node(Node('Arkadia'))
  G.add_node(Node('Argolis'))
  G.add_node(Node('Lakonia'))
  G.add_node(Node('Messenia'))
  G.add_node(Node('Hydrea'))
  G.add_node(Node('Seriphos'))
  G.add_node(Node('Melos'))
  G.add_node(Node('Kythera Island'))
  G.add_node(Node('Messara'))
  G.add_node(Node('Pephka'))
  G.add_node(Node('Thera'))
  G.add_node(Node('Anaphi'))
  G.add_node(Node('Nisyros'))
  G.add_node(Node('Paros'))
  G.add_node(Node('Naxos'))
  G.add_node(Node('Kos'))
  G.add_node(Node('Keos'))
  G.add_node(Node('Andros'))
  G.add_node(Node('Samos'))
  G.add_node(Node('Delos'))
  G.add_node(Node('Mykonos'))
  G.add_node(Node('Skyros'))
  G.add_node(Node('Euboea'))
  G.add_node(Node('Chios'))
  G.add_node(Node('Lemnos'))
  G.add_node(Node('Lesbos'))
  G.add_node(Node('Thasos'))

  #Adicionando Vértices
  G.add_edge('Kephallonia', 'Elis', 33)
  G.add_edge('Kephallonia', 'Achaia', 39)
  G.add_edge('Kephallonia', 'Phokis', 6)
  G.add_edge('Kephallonia', 'Megaris', 7)
  G.add_edge('Elis', 'Achaia', 6)
  G.add_edge('Elis', 'Arkadia', 2)
  G.add_edge('Achaia', 'Arkadia', 8)
  G.add_edge('Achaia', 'Korinthia', 21)
  G.add_edge('Arkadia', 'Messenia', 3)
  G.add_edge('Arkadia', 'Lakonia', 4)
  G.add_edge('Arkadia', 'Korinthia', 12)
  G.add_edge('Korinthia', 'Megaris', 11)
  G.add_edge('Korinthia', 'Argolis', 2)
  G.add_edge('Messenia', 'Lakonia', 1)
  G.add_edge('Messenia', 'Kythera Island', 9)
  G.add_edge('Argolis', 'Hydrea', 1)
  G.add_edge('Argolis', 'Seriphos', 2)
  G.add_edge('Argolis', 'Attika', 4)
  G.add_edge('Argolis', 'Lakonia', 13)
  G.add_edge('Lakonia', 'Hydrea', 15)
  G.add_edge('Lakonia', 'Melos', 16)
  G.add_edge('Hydrea', 'Seriphos', 1)
  G.add_edge('Hydrea', 'Melos', 2)
  G.add_edge('Seriphos', 'Melos', 3)
  G.add_edge('Seriphos', 'Keos', 2)
  G.add_edge('Megaris', 'Attika', 7)
  G.add_edge('Megaris', 'Boeotia', 26)
  G.add_edge('Attika', 'Boeotia', 17)
  G.add_edge('Attika', 'Euboea', 2)
  G.add_edge('Attika', 'Andros', 3)
  G.add_edge('Attika', 'Keos', 2)
  G.add_edge('Boeotia', 'Lokris', 21)
  G.add_edge('Boeotia', 'Phokis', 24)
  G.add_edge('Boeotia', 'Euboea', 20)
  G.add_edge('Phokis', 'Lokris', 2)
  G.add_edge('Phokis', 'Malis', 1)
  G.add_edge('Lokris', 'Malis', 1)
  G.add_edge('Lokris', 'Euboea', 2)
  G.add_edge('Euboea', 'Makedonia', 4)
  G.add_edge('Euboea', 'Lemnos', 26)
  G.add_edge('Euboea', 'Skyros', 2)
  G.add_edge('Malis', 'Makedonia', 2)
  G.add_edge('Makedonia', 'Thasos', 2)
  G.add_edge('Thasos', 'Lemnos', 2)
  G.add_edge('Thasos', 'Lesbos', 4)
  G.add_edge('Lemnos', 'Lesbos', 2)
  G.add_edge('Lemnos', 'Skyros', 27)
  G.add_edge('Lemnos', 'Chios', 3)
  G.add_edge('Skyros', 'Chios', 33)
  G.add_edge('Skyros', 'Andros', 2)
  G.add_edge('Chios', 'Samos', 18)
  G.add_edge('Andros', 'Samos', 16)
  G.add_edge('Andros', 'Keos', 5)
  G.add_edge('Andros', 'Delos', 13)
  G.add_edge('Andros', 'Mykonos', 14)
  G.add_edge('Keos', 'Delos', 7)
  G.add_edge('Keos', 'Paros', 6)
  G.add_edge('Delos', 'Mykonos', 1)
  G.add_edge('Delos', 'Paros', 1)
  G.add_edge('Delos', 'Naxos', 1)
  G.add_edge('Mykonos', 'Naxos', 1)
  G.add_edge('Mykonos', 'Paros', 1)
  G.add_edge('Paros', 'Naxos', 1)
  G.add_edge('Samos', 'Kos', 3)
  G.add_edge('Naxos', 'Kos', 1)
  G.add_edge('Paros', 'Thera', 7)
  G.add_edge('Melos', 'Thera', 10)
  G.add_edge('Thera', 'Anaphi', 1)
  G.add_edge('Thera', 'Messara', 3)
  G.add_edge('Anaphi', 'Messara', 4)
  G.add_edge('Kythera Island', 'Messara', 9)
  G.add_edge('Kos', 'Nisyros', 2)
  G.add_edge('Anaphi', 'Nisyros', 1)
  G.add_edge('Anaphi', 'Pephka', 3)
  G.add_edge('Nisyros', 'Pephka', 4)
  G.add_edge('Messara', 'Pephka', 2)

  # Execute the algorithm
  alg = UCS(G, begin, destiny)
  path, path_length = alg.search()
  path=" -> ".join(path)
  response = [path, path_length]
  return response