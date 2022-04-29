variavel = ['Anderson', 'Amanda', 'Aline', 'Katia', 'Edmilson']

for valor in variavel:
    if valor.lower().startswith('a'):
        print(f'Começa com A {valor}')
    else:
        print(f'Não começa com A {valor}')