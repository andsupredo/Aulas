entrada = input('Insira o CPF: ')
cpf = entrada.split(' ')

n1= int(cpf[0][0]) *10
n2= int(cpf[0][1]) * 9
n3= int(cpf[0][2]) * 8
n4= int(cpf[0][3]) * 7
n5= int(cpf[0][4]) * 6
n6= int(cpf[0][5]) * 5
n7= int(cpf[0][6]) * 4
n8= int(cpf[0][7]) * 3
n9= int(cpf[0][8]) * 2


soma1 = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9

d1_form = 11 - (soma1 % 11)
if d1_form == int(cpf[0][9]) or d1_form > 9 and d1_form <=11:
    d1 = True
else:
    print('CPF inválido')

n11= int(cpf[0][0]) * 11
n22= int(cpf[0][1]) * 10
n33= int(cpf[0][2]) * 9
n44= int(cpf[0][3]) * 8
n55= int(cpf[0][4]) * 7
n66= int(cpf[0][5]) * 6
n77= int(cpf[0][6]) * 5
n88= int(cpf[0][7]) * 4
n99= int(cpf[0][8]) * 3
if d1 == True:
    n10 = int(cpf[0][9]) * 2
soma2 = n11 + n22 + n33 + n44 + n55 + n66 + n77 + n88 + n99 + n10
d2_form = 11 - (soma2 % 11)
if d2_form == int(cpf[0][10]) or d1_form > 9 and d1_form <=11:
    d2 = True
    cpf = ' '.join(cpf)
    print(f'O cpf {cpf} é válido')
else:
    print('CPF inválido')