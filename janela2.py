import tkinter as tk

def imprimir_subtrair():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    print(f'O resultado sera de {n1} - {n2} e: {n1 - n2}')

def imprimir_somar():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    print(f'O resultado sera de {n1} + {n2} e: {n1 + n2}')

def imprimir_dividir():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    if(n2<=0):
        print("e impossil dividir esse numero por zero")
    else:
        print(f'O resultado sera de {n1} / {n2} e: {n1 / n2}')

def imprimir_multiplicar():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    print(f'O resultado sera de {n1} * {n2} e: {n1 * n2}')

janela = tk.Tk()

janela.configure(background='#43e0c1')
janela.geometry("900x800")
janela.title("calculadora")
janela.minsize(width=600, height=800)
janela.maxsize(width=1300,height=1600)
janela.resizable(True, True)

header = tk.Label(janela, text="Bem vindo")
header.pack()

numero1 = tk.Entry(fg="black",bg="#ccc",width=20)
numero1.pack()

numero2 = tk.Entry(fg="black",bg="#ccc", width=20)
numero2.pack()

btnMais = tk.Button(janela, text='+',width=5,command=imprimir_somar)
btnMais.pack()

btnSubtrair = tk.Button(janela, text='-',width=5,command=imprimir_subtrair)
btnSubtrair.pack()

btnDividir = tk.Button(janela, text='/',width=5,command=imprimir_dividir)
btnDividir.pack()

btnMultiplicar = tk.Button(janela, text='*',width=5,command=imprimir_multiplicar)
btnMultiplicar.pack()

# btn = tk.Button(janela, text="Enviar", command=imprimir_valor)
# btn.pack()

janela.mainloop()