def func(*args):
    args = list(args)
    for v in args:
        print(v)

func(1, 2, 3, 4, 5)

def func2 (*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    print(nome)

lista = [1, 2, 3]
lista2 = [5, 50, 500]
func2(*lista, lista2, nome='Anderson', sobrenome='Barbosa')