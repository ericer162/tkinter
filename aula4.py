###17/03/2025_aula04_atividade-01###
#numero = int(input("Digite um número inteiro: "))

#if numero % 2 == 0:
#    print(f"O número {numero} é par.")
#else:
#    print(f"O número {numero} é ímpar.")

###atividade-02###
#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

#if numero1 > numero2:
#    print(f"O maior número é {numero1}.")
#elif numero2 > numero1:
#    print(f"O maior número é {numero2}.")
#else:
#    print("Os dois números são iguais.")


###atividade-03###
#valor_produto = float(input("Digite o valor do produto: R$ "))

#if valor_produto > 100:
#    desconto = valor_produto * 0.10  
#    valor_final = valor_produto - desconto
#    print(f"O valor com 10% de desconto é: R$ {valor_final:.2f}")
#elif 50 <= valor_produto <= 100:
#    desconto = valor_produto * 0.05  
#    valor_final = valor_produto - desconto
#    print(f"O valor com 5% de desconto é: R$ {valor_final:.2f}")
#else:
#     print(f"O valor do produto sem desconto é: R$ {valor_produto:.2f}")


###atividade-04###
#idade = int(input("Qual é a sua idade? "))

#if idade >= 18:
#    print("Você é maior de idade.")
#else:
#    print("Você é menor de idade.")


###atividade-05###
#numero = float(input("Digite um número: "))

#if numero > 0:
#    print("O número é positivo.")
#elif numero < 0:
#    print("O número é negativo.")
#else:
#    print("O número é zero.")


###atividade-06###
#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))

#media = (nota1 + nota2) / 2

#if media >= 7:
#    print(f"A média foi {media}. Você foi aprovado!")
#elif media >= 5:
#    print(f"A média foi {media}. Você está de recuperação.")
#else:
#    print(f"A média foi {media}. Você foi reprovado.")


###atividade-07###
#num1=input('numero1 : ')
#num2=input('numero2 : ')
#operador=input("operador : ")

#def calcule(num1 , num2 , operador):
#    match(operador):
#        case("+"):
#            resultado=num1 + num2 
#        case("-"):
#            resultado=num1 - num2
#        case("*"):
#            resultado=num1 * num2
#        case("/"):
#            if(num2 == 0):
#                resultado='esse numero e indivisivel por zero'  
#            else:
#                resultado=num1 / num2

#    return resultado

#resultado=calcule(int(num1), int(num2),operador)

#print(f'{resultado}')


###atividade-08###
#lado1 = float(input("Digite o primeiro lado do triângulo: "))
#lado2 = float(input("Digite o segundo lado do triângulo: "))
#lado3 = float(input("Digite o terceiro lado do triângulo: "))

#if lado1 == lado2 == lado3:
#    print("O triângulo é equilátero (três lados iguais).")
#elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
#    print("O triângulo é isósceles (dois lados iguais).")
#else:
#    print("O triângulo é escaleno (três lados diferentes).")


###atividade-09###
#numero1 = int(input("Digite o primeiro número: "))
#numero2 = int(input("Digite o segundo número: "))

#if numero1 % numero2 == 0:
#    print(f"{numero1} é múltiplo de {numero2}.")
#else:
#    print(f"{numero1} não é múltiplo de {numero2}.")


###atividade-10###

celsius = float(input("Digite a temperatura em graus Celsius: "))

escolha = input("Para qual escala deseja converter? (Fahrenheit/F ou Kelvin/K): ").strip().upper()

if escolha == 'F' or escolha == 'FAHRENHEIT':
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é equivalente a {fahrenheit}°F.")
elif escolha == 'K' or escolha == 'KELVIN':
    kelvin = celsius + 273.15
    print(f"{celsius}°C é equivalente a {kelvin}K.")
else:
    print("Escala inválida! Por favor, escolha 'F' para Fahrenheit ou 'K' para Kelvin.")