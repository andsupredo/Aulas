def div(n1, n2):
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite mais um número inteiro: '))
    if n2 == 0:
        print("Impossível dividir por 0")
    else:
        print(int(n1/n2))
    if n1 % n2 != 0:
        mod = n1 % n2
        print(f'O Módulo da divisão é: {mod}')

divisao = div(n1=(), n2=())