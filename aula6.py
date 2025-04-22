###atividade-01_parte02###
# n = int(input("Digite um número inteiro N: "))
# fibonacci = [0, 1]
# if n == 1:
#     print([0])
# elif n == 2:
#     print(fibonacci)
# elif n > 2:
#     for i in range(2, n):
#         proximo = fibonacci[i-1] + fibonacci[i-2]
#         fibonacci.append(proximo)
#     print(fibonacci)
# else:
#     print("Por favor, digite um número inteiro positivo maior que zero.")


###atividade-02###
# print("Múltiplos de 3 entre 1 e 30:")
# for numero in range(1, 31):
#     if numero % 3 == 0:
#         print(numero)



###atividade-03###
soma = 0
for numero in range(1, 51):
    if numero % 2 != 0:  
        soma += numero
print("A soma dos números ímpares de 1 a 50 é:", soma)