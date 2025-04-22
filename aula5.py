###atividade-01_24/03/2025###
#  for numero in range(1, 21):
#     if numero % 2 == 0:
#         print(numero)


###atividade-02###
# numero = int(input("Digite um número para ver sua tabuada: "))
# print(f"\nTabuada do {numero}:")
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")


###atividade-03###
# for contador in range(10, 0, -1):
#    print(contador)
# print("FIM!")


###atividade-04###
# soma = 0  
# print("Digite 5 números para serem somados:")
# for i in range(1, 6):  
#    numero = float(input(f"Número {i}: "))  
#    soma += numero  
# print(f"\nA soma dos números é: {soma}")


###atividade-05###
palavra = input("Digite uma palavra: ").lower() 
vogais = "aeiou"
contador = 0
for letra in palavra:
   if letra in vogais:
       contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")