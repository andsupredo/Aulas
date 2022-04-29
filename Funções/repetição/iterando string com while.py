#variável
frase = "o anderson está estudando ti"
#variável que traz o tamanho da frase
tamanho_frase = len(frase)
#variável que irá aumentando conforme o laço avança
contador = 0
#variável que irá sendo agregada a cada passagem do laço
nova_string = ""
#esse while irá acontecer ate que o contador tenha o mesmo tamanho da frase completa (tamanho que foi contado pelo len)
while contador < tamanho_frase:
    #nova_string sendo iterada com a frase
    nova_string += frase[contador]
    #variavel que esta controlando com +1 iteração a cada laço
    contador +=1
    print(nova_string)