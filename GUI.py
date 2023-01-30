import tkinter as tk
from tkinter import messagebox
from arquivo import *


def salva_entrada():
    """Salva entrada do usuario em JSON e zera valor do objeto StringVar"""
    cpf = str_entrada.get()
    Arquivo.escreve_json(Arquivo.JSON_ENTRADA, {'cpf': cpf})
    str_entrada.set("")
    return cpf    # retorna valor da entrada para impressão de log no console


def recebe_retorno(log):
    """Recebe retorno de validação do back end e gera messagebox para o usuário"""    
    retorno = Arquivo.le_json(Arquivo.JSON_RETORNO)
    if retorno['msg']:
        print(f'{log} -> {retorno["msg"]}')  # impressão de log no console
        if 'OK' in retorno['msg']:
            messagebox.showinfo("Sucesso", retorno['msg'])
        else:
            messagebox.showerror("Falha", retorno['msg'])                
    Arquivo.escreve_json(Arquivo.JSON_RETORNO, {'msg': ''})
   

def cpf_io():
    """Gerencia o ciclo de entrada e saida da validação de cpf"""
    log = salva_entrada()  # variável que copia entrada para imprimir log no console 
    time.sleep(0.5)
    recebe_retorno(log)


"""Bloco de geração da Graphic User Interface"""

root = tk.Tk()  # instanciação do objeto da janela base da interface gráfica
imagem = tk.PhotoImage(file='fundo.png').subsample(1)   # arquivo do pano de fundo da GUI
root.title('AVALIAÇÃO FINAL PYTHON SENAC-TECH')    # Nome da Aplicação
root.geometry('600x400')   # tamanho da janela da aplicação (pixels)
root.resizable(width=False, height=False)  # configuração do ajuste do tamanho da janela (imutável)
root.iconbitmap('icone.ico')           # arquivo com icone exibido na janela da aplicação
fundo = tk.Label(root, image=imagem, )  # labem com a imagem de fundo da janela
lbl_1 = tk.Label(root, text='CPF VALIDATOR TABAJARA',    
                font=("Arial", 30), fg='white', background='#ff6a11') # label principal com a funcionalidade da aplicação
lbl_2 = tk.Label(root, text='Digite apenas números OU formato tracicional XXX.XXX.XXX-XX',
                font=("Arial", 10), fg='black', background='#ff6a11') # label secundário com a instruções ao usuário
str_entrada = tk.StringVar()  # objeto StringVar que recebe entrada do usuário                    
entry = tk.Entry(root, font=("Arial Bold", 30),  
                width=13, textvariable=str_entrada)   # campo de entrada de dados pelo usuário
btn_validar = tk.Button(root, text='VALIDAR',
                        command=cpf_io, font=('Arial', 20), bg='light green')  # botão solicitação de validação 
btn_fechar = tk.Button(root, text='FECHAR',
                    command=root.destroy, bg='red', font=('Arial', 15))  # botão para fechar janela
fundo.place(x=0, relheight=1., relwidth=1.)
lbl_1.pack(pady=8)    # daqui para baixo, comandos para exibição dos elementos na janela
lbl_2.pack()
entry.pack()
btn_validar.pack(pady=20)
btn_fechar.pack(side='bottom', pady=25)
root.mainloop()

"""Fim do Bloco"""