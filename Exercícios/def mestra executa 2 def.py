def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def ola(nome):
    return f'olá, {nome}!'

def adeus(nome, adeus):
    return f'{adeus}, {nome}!'

exec = mestre(ola, 'Anderson')
print(exec)

exec2 = mestre(adeus, 'Anderson', 'Adeus')
print(exec2)