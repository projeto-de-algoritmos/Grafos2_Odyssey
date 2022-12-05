import networkx as nx
import matplotlib.pyplot as plt

#Cria grafo vazio
G = nx.Graph()

#Adiciona Vértices
G.add_node('Kephallonia')
G.add_node('Phokis')
G.add_node('Malis')
G.add_node('Lokris')
G.add_node('Boeotia')
G.add_node('Makedonia')
G.add_node('Megaris')
G.add_node('Attika')
G.add_node('Korinthia')
G.add_node('Achaia')
G.add_node('Elis')
G.add_node('Arkadia')
G.add_node('Argolis')
G.add_node('Lakonia')
G.add_node('Messenia')
G.add_node('Hydrea')
G.add_node('Seriphos')
G.add_node('Melos')
G.add_node('Kythera Island')
G.add_node('Messara')
G.add_node('Pephka')
G.add_node('Thera')
G.add_node('Anaphi')
G.add_node('Nisyros')
G.add_node('Paros')
G.add_node('Naxos')
G.add_node('Kos')
G.add_node('Keos')
G.add_node('Andros')
G.add_node('Samos')
G.add_node('Delos')
G.add_node('Mykonos')
G.add_node('Skyros')
G.add_node('Euboea')
G.add_node('Chios')
G.add_node('Lemnos')
G.add_node('Lesbos')
G.add_node('Thasos')

#Adicionando Vértices
G.add_edge('Kephallonia', 'Elis')
G.add_edge('Kephallonia', 'Achaia')
G.add_edge('Kephallonia', 'Phokis')
G.add_edge('Kephallonia', 'Megaris')
G.add_edge('Elis', 'Achaia')
G.add_edge('Elis', 'Arkadia')
G.add_edge('Achaia', 'Arkadia')
G.add_edge('Achaia', 'Korinthia')
G.add_edge('Arkadia', 'Messenia')
G.add_edge('Arkadia', 'Lakonia')
G.add_edge('Arkadia', 'Korinthia')
G.add_edge('Korinthia', 'Megaris')
G.add_edge('Korinthia', 'Argolis')
G.add_edge('Messenia', 'Lakonia')
G.add_edge('Messenia', 'Kythera Island')
G.add_edge('Argolis', 'Hydrea')
G.add_edge('Argolis', 'Seriphos')
G.add_edge('Argolis', 'Attika')
G.add_edge('Argolis', 'Lakonia')
G.add_edge('Lakonia', 'Hydrea')
G.add_edge('Lakonia', 'Melos')
G.add_edge('Hydrea', 'Seriphos')
G.add_edge('Hydrea', 'Melos')
G.add_edge('Seriphos', 'Melos')
G.add_edge('Seriphos', 'Keos')
G.add_edge('Megaris', 'Attika')
G.add_edge('Megaris', 'Boeotia')
G.add_edge('Attika', 'Boeotia')
G.add_edge('Attika', 'Euboea')
G.add_edge('Attika', 'Andros')
G.add_edge('Attika', 'Keos')
G.add_edge('Boeotia', 'Lokris')
G.add_edge('Boeotia', 'Phokis')
G.add_edge('Boeotia', 'Euboea')
G.add_edge('Phokis', 'Lokris')
G.add_edge('Phokis', 'Malis')
G.add_edge('Lokris', 'Malis')
G.add_edge('Lokris', 'Euboea')
G.add_edge('Euboea', 'Makedonia')
G.add_edge('Euboea', 'Lemnos')
G.add_edge('Euboea', 'Skyros')
G.add_edge('Malis', 'Makedonia')
G.add_edge('Makedonia', 'Thasos')
G.add_edge('Thasos', 'Lemnos')
G.add_edge('Thasos', 'Lesbos')
G.add_edge('Lemnos', 'Lesbos')
G.add_edge('Lemnos', 'Skyros')
G.add_edge('Lemnos', 'Chios')
G.add_edge('Skyros', 'Chios')
G.add_edge('Skyros', 'Andros')
G.add_edge('Chios', 'Samos')
G.add_edge('Andros', 'Samos')
G.add_edge('Andros', 'Keos')
G.add_edge('Andros', 'Delos')
G.add_edge('Andros', 'Mykonos')
G.add_edge('Keos', 'Delos')
G.add_edge('Keos', 'Paros')
G.add_edge('Delos', 'Mykonos')
G.add_edge('Delos', 'Paros')
G.add_edge('Delos', 'Naxos')
G.add_edge('Mykonos', 'Naxos')
G.add_edge('Mykonos', 'Paros')
G.add_edge('Paros', 'Naxos')
G.add_edge('Samos', 'Kos')
G.add_edge('Naxos', 'Kos')
G.add_edge('Paros', 'Thera')
G.add_edge('Melos', 'Thera')
G.add_edge('Thera', 'Anaphi')
G.add_edge('Thera', 'Messara')
G.add_edge('Anaphi', 'Messara')
G.add_edge('Kythera Island', 'Messara')
G.add_edge('Kos', 'Nisyros')
G.add_edge('Anaphi', 'Nisyros')
G.add_edge('Anaphi', 'Pephka')
G.add_edge('Nisyros', 'Pephka')
G.add_edge('Messara', 'Pephka')

#Adicionando pesos aos vértices
G['Kephallonia']['Elis']['peso'] = 33
G['Kephallonia']['Achaia']['peso'] = 39
G['Kephallonia']['Phokis']['peso'] = 6
G['Kephallonia']['Megaris']['peso'] = 7
G['Elis']['Achaia']['peso'] = 6
G['Elis']['Arkadia']['peso'] = 2
G['Achaia']['Arkadia']['peso'] = 8
G['Achaia']['Korinthia']['peso'] = 21
G['Arkadia']['Messenia']['peso'] = 3
G['Arkadia']['Lakonia']['peso'] = 4
G['Arkadia']['Korinthia']['peso'] = 12
G['Korinthia']['Megaris']['peso'] = 11
G['Korinthia']['Argolis']['peso'] = 2
G['Messenia']['Lakonia']['peso'] = 1
G['Messenia']['Kythera Island']['peso'] = 9
G['Argolis']['Hydrea']['peso'] = 1
G['Argolis']['Seriphos']['peso'] = 2
G['Argolis']['Attika']['peso'] = 4
G['Argolis']['Lakonia']['peso'] = 13
G['Lakonia']['Hydrea']['peso'] = 15
G['Lakonia']['Melos']['peso'] = 16
G['Hydrea']['Seriphos']['peso'] = 1
G['Hydrea']['Melos']['peso'] = 2
G['Seriphos']['Melos']['peso'] = 3
G['Seriphos']['Keos']['peso'] = 2
G['Megaris']['Attika']['peso'] = 7
G['Megaris']['Boeotia']['peso'] = 26
G['Attika']['Boeotia']['peso'] = 17
G['Attika']['Euboea']['peso'] = 2
G['Attika']['Andros']['peso'] = 3
G['Attika']['Keos']['peso'] = 2
G['Boeotia']['Lokris']['peso'] = 21
G['Boeotia']['Phokis']['peso'] = 24
G['Boeotia']['Euboea']['peso'] = 20
G['Phokis']['Lokris']['peso'] = 2
G['Phokis']['Malis']['peso'] = 1
G['Lokris']['Malis']['peso'] = 1
G['Lokris']['Euboea']['peso'] = 2
G['Euboea']['Makedonia']['peso'] = 4
G['Euboea']['Lemnos']['peso'] = 26
G['Euboea']['Skyros']['peso'] = 2
G['Malis']['Makedonia']['peso'] = 2
G['Makedonia']['Thasos']['peso'] = 2
G['Thasos']['Lemnos']['peso'] = 2
G['Thasos']['Lesbos']['peso'] = 4
G['Lemnos']['Lesbos']['peso'] = 2
G['Lemnos']['Skyros']['peso'] = 27
G['Lemnos']['Chios']['peso'] = 3
G['Skyros']['Chios']['peso'] = 33
G['Skyros']['Andros']['peso'] = 2
G['Chios']['Samos']['peso'] = 18
G['Andros']['Samos']['peso'] = 16
G['Andros']['Keos']['peso'] = 5
G['Andros']['Delos']['peso'] = 13
G['Andros']['Mykonos']['peso'] = 14
G['Keos']['Delos']['peso'] = 7
G['Keos']['Paros']['peso'] = 6
G['Delos']['Mykonos']['peso'] = 1
G['Delos']['Paros']['peso'] = 1
G['Delos']['Naxos']['peso'] = 1
G['Mykonos']['Naxos']['peso'] = 1
G['Mykonos']['Paros']['peso'] = 1
G['Paros']['Naxos']['peso'] = 1
G['Samos']['Kos']['peso'] = 3
G['Naxos']['Kos']['peso'] = 1
G['Paros']['Thera']['peso'] = 7
G['Melos']['Thera']['peso'] = 10
G['Thera']['Anaphi']['peso'] = 1
G['Thera']['Messara']['peso'] = 3
G['Anaphi']['Messara']['peso'] = 4
G['Kythera Island']['Messara']['peso'] = 9
G['Kos']['Nisyros']['peso'] = 2
G['Anaphi']['Nisyros']['peso'] = 1
G['Anaphi']['Pephka']['peso'] = 3
G['Nisyros']['Pephka']['peso'] = 4
G['Messara']['Pephka']['peso'] = 2

#Listando pesos de cada aresta
print ('Listando as dificuldades dos trajetos')
for edge in G.edges():
    u = edge[0]
    v = edge[1]
    print ('A dificuldade de fazer o trajeto ', edge, 'é de ', G[u][v]['peso'])

print('Plotando grafo como imagem. Verifique o arquivo graph.png.')
f = plt.figure(1)
f.set_figwidth(10)
f.set_figheight(10)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.savefig('graph.png')