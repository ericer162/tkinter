import tkinter as tk
janela= tk.Tk()

nome = "eric"
saudacao = tk.Label(text=f"OLA,dev {nome}")
saudacao.pack()

label = tk.Label(
    text="Hello, TKinter",
    fg="white",
    bg="black",
    width=10,
    height=10,
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

# tk.Entry(fg="yellow", bg="blue",width=50)
janela.mainloop()
