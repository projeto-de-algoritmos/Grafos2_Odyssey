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

for k in range(len(arv_ger_min)):
    if arv_ger_min[k][0] == raiz and arv_ger_min[k][1] == final:
        finalList.append(arv_ger_min[k])
    else:
        for j in range(k + 1, len(arv_ger_min)):
            if(arv_ger_min[k][1] == arv_ger_min[j][0]):
                # print(f'primeiro:{arv_ger_min[k]}, {arv_ger_min[j]}')
                if arv_ger_min[k] not in finalList:
                    finalList.append(arv_ger_min[k])
                if arv_ger_min[j] not in finalList:
                    finalList.append(arv_ger_min[j])
        for g in range(k-1, len(arv_ger_min)):
             if(arv_ger_min[g][1] != arv_ger_min[k][0]):
                if(arv_ger_min[k][1] != arv_ger_min[j][0]):
                    finalList.pop(arv_ger_min[g])
                else:
                    finalList.pop(arv_ger_min[k])

print(finalList)
