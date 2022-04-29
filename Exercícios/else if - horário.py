hora = input("Que horas são? ")

try:
    hora = int(hora)

    if hora >= 1 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print ("Boa noite!")
    else:
        print ("Erro! Valor inserido não é uma hora válida!")

except:
    print("Erro! Valor inserido não é uma hora válida!")