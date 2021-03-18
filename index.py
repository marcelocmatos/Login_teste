# Bibliotecas
from tkinter import *
from tkinter import ttk
# from tkinter import messagebox

# Definir a Janela
jan = Tk()
jan.title('DDP Systems - Painel de Acesso')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.95)
jan.iconbitmap(default='icons/LogoIcon.ico')

# Carregar Imagens
logo = PhotoImage(file='icons/logo.png')

# Rótulos
frame_esq = Frame(jan, width=200, height=300, bg='DarkOliveGreen4', relief='raise')
frame_esq.pack(side=LEFT)
frame_dir = Frame(jan, width=395, height=300, bg='DarkOliveGreen4', relief='raise')
frame_dir.pack(side=RIGHT)

logo_label = Label(frame_esq, image=logo, bg='DarkOliveGreen4')
logo_label.place(x=50, y=100)

rotulo_usuario = Label(frame_dir, text='Usuário:', font=('Century Gothic', 20), bg='DarkOliveGreen4', fg='White')
rotulo_usuario.place(x=5, y=105)
usuario = ttk.Entry(frame_dir, width=40)
usuario.place(x=120, y=120)
rotulo_senha = Label(frame_dir, text='Senha:', font=('Century Gothic', 20), bg='DarkOliveGreen4', fg='White')
rotulo_senha.place(x=5, y=155)
senha = ttk.Entry(frame_dir, width=40, show='☠️')
senha.place(x=120, y=165)

# Botões
botao_acesso = ttk.Button(frame_dir, text='Entrar', width=20)
botao_acesso.place(x=90, y=205)

def cadastro():
	botao_acesso.place(x=5000)
	botao_registro.place(x=5000)
	rotulo_nome = Label(frame_dir, text='Nome:', font=('Century Gothic', 20), bg='DarkOliveGreen4', fg='White')
	rotulo_email = Label(frame_dir, text='E-mail:', font=('Century Gothic', 20), bg='DarkOliveGreen4', fg='White')
	rotulo_nome.place(x=5, y=15)
	rotulo_email.place(x=5, y=60)

	email = ttk.Entry(frame_dir, width=40)
	nome = ttk.Entry(frame_dir, width=40)
	email.place(x=120, y=75)
	nome.place(x=120, y=30)

	def voltar():
		botao_cadastro.place(x=5000)
		botao_voltar.place(x=5000)
		rotulo_nome.place(x=5000)
		rotulo_email.place(x=5000)
		email.place(x=5000)
		nome.place(x=5000)
		botao_acesso.place(x=90, y=205)
		botao_registro.place(x=230, y=205)

	botao_cadastro = ttk.Button(frame_dir, text='Cadastrar', width=20)
	botao_voltar = ttk.Button(frame_dir, text='Voltar', width=20, command=voltar)



	botao_cadastro.place(x=230, y=205)
	botao_voltar.place(x=90, y=205)	

botao_registro = ttk.Button(frame_dir, text='Cadastro', width=20, command=cadastro)
botao_registro.place(x=230, y=205)






jan.mainloop()
