def percentual(n1, n2):
    n2 = n1 * (n2/100)
    return n1 + n2

percent = percentual(int(input('valor inteiro: ')), int(input('valor inteiro para acrescentar percentualmente: ')))

print(percent)