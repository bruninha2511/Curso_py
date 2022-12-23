import tkinter
from tkinter import *
from tkinter import ttk

co0 = '#444466'
co1 = '#feffff'
co2 = '#6f9fbd'

fundodia = '#6cc4cc'
fundonoite = '#484f60'
fundotarde = '#bfb86d'
fundo = fundodia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frametop = Frame(janela, width=320, height=50, bg=co1,pady=0, padx=0)
frametop.grid(row=1, column=0)

framecorpo = Frame(janela, width=320, height=300, bg=fundo,pady=12, padx=0)
framecorpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

elocal = Entry(frametop, width=20, justify='left', font=('', 14), highlightthickness=1, relief='solid')
elocal.place(x=15, y=10)
bver = Button(frametop,text='Ver clima' ,bg=co1, fg=co2, font=('Ivy 9 bold'), relief='raised', overrelief=RIDGE)
bver.place(x=250, y=10)

l_cidade = Label(framecorpo, text='Cabinda Angola Africa', anchor='center', bg=fundo, fg=co1, font=("Arial 14")) 
l_cidade.place(x=10, y=4)

l_data = Label (framecorpo, text='09 03 2022 | 10:50:00 AM', anchor='center', bg=fundo, fg=co1, font=("Arial 10")) 
l_data.place(x=10, y=54)

l_humidade = Label (framecorpo, text='84', anchor='center', bg=fundo, fg=co1, font=("Arial 45"))
l_humidade.place(x=10, y=100)

l_h_simbol = Label(framecorpo, text='%', anchor='center', bg=fundo, fg=co1, font=("Arial 10 bold")) 
l_h_simbol.place(x=85, y=110)

l_h_nome = Label (framecorpo, text='Humidade', anchor='center', bg=fundo, fg=co1, font=("Arial 8"))
l_h_nome.place(x=85, y=140) 

l_pressao = Label (framecorpo, text='Pressão: 1000', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(framecorpo, text='Velocidade do vento: 1000', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_velocidade.place(x=10, y=212)





janela.mainloop()
