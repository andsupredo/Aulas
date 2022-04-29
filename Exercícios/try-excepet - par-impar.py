num1 = input("digite um número inteiro: ")

try:
    num1 = int(num1)
    if num1 % 2 == 0:
        print("O número", num1, "é par!")
    else:
        print("O número", num1, "é impar!")
except:
    print("O valor inserido não corresponde a um número inteiro")

