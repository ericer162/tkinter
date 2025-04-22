print("Hello World (ola mundo)!! :")

f= ("ola mundo")
print(f)

print(f'A frase e: "{f}"')

nome =input("Digite seu nome: ")
num1 = input('numero 1: ')
num2 = input('numero 2: ')
operador=input("operador : ")

def calcule(num1 , num2 , operador):
    match(operador):
        case("+"):
            resultado=num1 + num2 
        case("-"):
            resultado=num1 - num2
        case("*"):
            resultado=num1 * num2
        case("/"):
            if(num2 == 0):
                resultado='esse numero e indivisivel por zero'  
            else:
                resultado=num1 / num2

    return resultado

resultado=calcule(int(num1), int(num2),operador)

print(f"{resultado}")


nome = input("Digite o nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
##input++
valor1= input("informe seu valor: ")
valor2= input("informe seu valor: ")
soma=int("valor1")+("valor2")
