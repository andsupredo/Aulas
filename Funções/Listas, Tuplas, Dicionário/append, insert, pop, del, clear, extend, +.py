l1 = [1, 2, 3, 4, 5, 6]
l2 = [4, 5, 6, 7, 8, 9]


print(l1)
print(l2)
print()
print(l1[0]) #imprime so o item 0 da lista
print(l1[0:5:2]) #imprime do item 0 ao 5 ao passo de 2
print()
l3 = l1 + l2 #concatena 2 Listas, Tuplas, Dicionário
print(f'lista l3:{[l3]}')
print()
l2.append(10) #add um item no final da lista
print(l2)
print()
l1.insert(0, 0) #add um item na posição indicada na lista
print(l1)
print()
l1.pop(6) #deleta o ultimo item da lista
print(l1)
print()
del(l1[1:3]) #deleta o item indicado da lista a partir do 1 ao 3
print(l1)
print()
print(max(l2)) #maior valor da lista
print(min(l2)) # menor valor da lista
print()

for valor in l2: #imprime cada um dos itens separadamente em valor
    print(valor)
print()
l2 = list(range(4, 12, 2)) #imprime os itens utilizando o range
print(l2)

