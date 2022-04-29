l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

"""l_soma = []
for i in range(len(l2)):
   l_soma.append(l1[i] + l2[i])
print(l_soma)"""

l_soma = [x+y for x,y in zip(l1, l2)]
print(l_soma)

#OUUUUUUUUUU

from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]