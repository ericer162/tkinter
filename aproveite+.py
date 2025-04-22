import tkinter as tk

janela = tk.Tk()
janela.title("Sua Janela") # Adicione um título para a janela

logo = tk.PhotoImage(file='aula_15\\images\\logo.png')
logo = logo.subsample(3,3)
lb_logo = tk.Label(janela, image=logo, background='#00513f')    
lb_logo.grid(row=0, column=0)

lb_title = tk.Label(text='Aproveite+', font=('Georgia', 50), background='#00513f', fg='#42f5ef')
lb_title.grid(row=1, column=0)

lb_user = tk.Label(text='Usuário', font=15, background='#00513f', fg='#42f5ef')
lb_user.grid(row=3, column=0, pady=(50, 0))
lb_inputUser = tk.Entry()
lb_inputUser.grid(row=4, column=0, pady=(0,20))

lb_pass = tk.Label(text='Senha', font=15, background='#00513f', fg='#42f5ef')
lb_pass.grid(row=5, column=0)
lb_inputUser = tk.Entry()
lb_inputUser.grid(row=6, column=0, pady=(0,20))

bt1 = tk.Button(text="Enviar", font=("Georgia", 18), bg='#00513f', fg='white', bd=0, highlightthickness=0)
bt1.grid(row=7, column=0, ipadx=700)

window_width = 600
window_height = 400

janela.config(background='#00513f')
janela.geometry('1520x900+0+0')
janela.mainloop() 