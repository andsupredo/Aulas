variavel = 'nome'

def func():
    print(variavel)

def func2():
    #variavel criada apenas no escopo local
    variavel = 'outro nome'
    print(variavel)

func()
func2()

print(variavel)