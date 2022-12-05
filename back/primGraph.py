import heapq

# n, m = input().split()
n = 9
m = 14
final = 4

H = []
n_out = [[]*n for i in range(n)]

for j in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    n_out[a].append((b,c))
    n_out[b].append((a,c))

raiz = 0
for(x, c) in n_out[raiz]:
    heapq.heappush(H, (c, raiz, x))

n_edges = 0
custo_tot = 0
marcados = [raiz]
arv_ger_min = []

while n_edges < n-1:
    while True:
        (c, a, b) = heapq.heappop(H)
        if b not in marcados:
            break

    marcados.append(b)
    custo_tot += c
    arv_ger_min.append((a,b))
    n_edges += 1
    for (x,c) in n_out[b]:
        if x not in marcados:
            heapq.heappush(H, (c, b, x))

# print(custo_tot)
print(arv_ger_min)

finalList = []

j=1

#Criação do menor caminho possível entre o nó inicial e o nó final
def teste(j):
    for k in range(len(arv_ger_min)):
        if(j == len(arv_ger_min)):
            return arv_ger_min
        elif(k+1 != j):
            k = 0
            j = 1
        elif(arv_ger_min[k][1] != arv_ger_min[j][0]):
            arv_ger_min.remove(arv_ger_min[k])
            teste(j)      
        j += 1
                
teste(j)