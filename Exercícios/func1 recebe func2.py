def func():
    return 'Alô!'

def func2(funcao):
    return func()

var = func2(func)
print(var)