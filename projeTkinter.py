from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox

class Janelas:
    def __init__(self,master):
        self.root = master
        self.frame_pai = Frame(self.root)
        self.frame_pai.pack()
#--------------- frame pricipal ------------------------------------------------
        self.frame_01 = Frame(self.frame_pai)
        self.frame_01['bd'] = 10
        self.frame_01['relief'] = RIDGE
        self.frame_01['bg'] = 'blue'
        self.frame_01.grid(row=0,column=0)

        self.frame_02 = Frame(self.frame_01)
        self.frame_02['bd'] = 5
        self.frame_02['relief'] = RIDGE
        self.frame_02['bg'] = '#3CB371'
        self.frame_02.grid(row=0,column=0)
#-------------------------------------------------------------------------------
        self.frame_03 = Frame(self.frame_02)
        self.frame_03['bd'] = 5
        self.frame_03['relief'] = RIDGE
        self.frame_03['bg'] = '#00FF00'
        self.frame_03.grid(row=0,column=0,sticky=W)

        self.frame_04 = Frame(self.frame_03)
        self.frame_04['bd'] = 5
        self.frame_04['relief'] = RIDGE
        self.frame_04['bg'] = 'yellow'
        self.frame_04.grid(row=0,column=0)
#-------------------------------------------------------------------------------
        self.frame_05 = Frame(self.frame_02)
        self.frame_05['bd'] = 5
        self.frame_05['relief'] = RIDGE
        self.frame_05['bg'] = 'green'
        self.frame_05.grid(row=1,column=0,sticky=W,padx=430)

        self.frame_06 = Frame(self.frame_05)
        self.frame_06['bd'] = 5
        self.frame_06['relief'] = RIDGE
        self.frame_06['bg'] = 'yellow'
        self.frame_06.grid(row=0,column=1)
#-------------------------------------------------------------------------------
        self.frame_07 = Frame(self.frame_02)
        self.frame_07['bd'] = 5
        self.frame_07['relief'] = RIDGE
        self.frame_07['bg'] = 'green'
        self.frame_07.grid(row=1,column=0,sticky=W,pady=5)

        self.frame_08 = Frame(self.frame_07)
        self.frame_08['bd'] = 5
        self.frame_08['relief'] = RIDGE
        self.frame_08['bg'] = 'blue'
        self.frame_08.grid(row=0,column=0)
#-------------------- frame trieevem --------------------------------------------------------
        self.frame_09 = Frame(self.frame_02)
        self.frame_09['bd'] = 5
        self.frame_09['relief'] = RIDGE
        self.frame_09['bg'] = 'green'
        self.frame_09.grid(row=2,column=0,sticky=W)

        self.frame_10 = Frame(self.frame_09)
        self.frame_10['bd'] = 5
        self.frame_10['relief'] = RIDGE
        self.frame_10['bg'] = 'blue'
        self.frame_10.grid(row=0,column=0)

# ------------------ frame button ----------------------------------------------

        self.frame_11 = Frame(self.frame_02)
        self.frame_11['bd'] = 5
        self.frame_11['relief'] = RIDGE
        self.frame_11['bg'] = 'green'
        self.frame_11.grid(row=3,column=0,sticky=W)

        self.frame_12 = Frame(self.frame_11)
        self.frame_12['bd'] = 5
        self.frame_12['relief'] = RIDGE
        self.frame_12['bg'] = 'blue'
        self.frame_12.grid(row=1,column=0)

#------------------------------------------------------------------------------
        self.frame_13 = Frame(self.frame_02)
        self.frame_13['bd'] = 5
        self.frame_13['relief'] = RIDGE
        self.frame_13['bg'] = 'green'
        self.frame_13.grid(row=0,column=1,sticky=W)

        self.frame_14 = Frame(self.frame_13)
        self.frame_14['bd'] = 5
        self.frame_14['relief'] = RIDGE
        self.frame_14['bg'] = 'blue'
        self.frame_14.grid(row=1,column=0)



#----------------------- lebal titulo  ------------------------------------------------------
        self.label_frame5 = Label(self.frame_03,padx=253)
        self.label_frame5['bg'] = 'orange'
        self.label_frame5['text'] = 'CADASTRO DE PESSOAS'
        self.label_frame5['font'] = ('Arial 20 bold')
        self.label_frame5.grid(row=0,column=0)
#--------------- label_nome com entry_nome -------------------------------
        self.label_nome = Label(self.frame_07)
        self.label_nome['bd'] = 5
        self.label_nome['bg'] = '#00BFFF'
        self.label_nome['relief'] = RIDGE
        self.label_nome['text'] = 'Nome:'
        self.label_nome['font'] = ('Arial 20')
        self.label_nome.grid(row=0,column=0,sticky=W)

        self.entry_nome = Entry(self.frame_07)
        self.entry_nome['bd'] = 5
        self.entry_nome['font'] = ('Arial 20')
        self.entry_nome['bg'] = '#00BFFF'
        self.entry_nome['relief'] = SUNKEN
        self.entry_nome.grid(row=0,column=1)
#------------     label_cpf e entry_cpf --------------------------------------
        self.label_cpf = Label(self.frame_07,padx=15)
        self.label_cpf['bd'] = 5
        self.label_cpf['bg'] = '#00BFFF'
        self.label_cpf['relief'] = RIDGE
        self.label_cpf['text'] = 'Cpf:'
        self.label_cpf['font'] = ('Arial 20')
        self.label_cpf.grid(row=2,column=0,sticky=W)

        self.entry_cpf = Entry(self.frame_07)
        self.entry_cpf['bd'] = 5
        self.entry_cpf['relief'] = SUNKEN
        self.entry_cpf['bg'] = '#00BFFF'
        self.entry_cpf['font'] = ('Arial 20')
        self.entry_cpf.grid(row=2,column=1)
#----------------------  fome --------------------------------------------------
        self.label_fome = Label(self.frame_07,padx=2)
        self.label_fome['bd'] = 5
        self.label_fome['bg'] = '#00BFFF'
        self.label_fome['relief'] = RIDGE
        self.label_fome['text'] = 'Fome:'
        self.label_fome['font'] = ('Arial 20')
        self.label_fome.grid(row=3,column=0,sticky=W)

        self.entry_fome = Entry(self.frame_07)
        self.entry_fome['bd'] = 5
        self.entry_fome['relief'] = SUNKEN
        self.entry_fome['bg'] = '#00BFFF'
        self.entry_fome['font'] = ('Arial 20')
        self.entry_fome.grid(row=3,column=1)
#-------------------label_uf entry_uf ---------------------------------------------------------
        self.label_uf = Label(self.frame_05,padx=30)
        self.label_uf['bd'] = 5
        self.label_uf['bg'] = '#00BFFF'
        self.label_uf['relief'] = RIDGE
        self.label_uf['text'] = 'Uf:'
        self.label_uf['font'] = ('Arial 20')
        self.label_uf.grid(row=0,column=0,sticky=W)

        self.entry_uf = Entry(self.frame_05)
        self.entry_uf['bd'] = 5
        self.entry_uf['relief'] = SUNKEN
        self.entry_uf['bg'] = '#00BFFF'
        self.entry_uf['font'] = ('Arial 20')
        self.entry_uf.grid(row=0,column=1)
#-----------------  label_barrio e entry_cidade -----------------------------------------------------------
        self.label_cidade = Label(self.frame_05)
        self.label_cidade['bd'] = 5
        self.label_cidade['bg'] = '#00BFFF'
        self.label_cidade['relief'] = RIDGE
        self.label_cidade['text'] = 'Cidade:'
        self.label_cidade['font'] = ('Arial 20')
        self.label_cidade.grid(row=1,column=0)

        self.entry_cidade = Entry(self.frame_05)
        self.entry_cidade['bd'] = 5
        self.entry_cidade['relief'] = SUNKEN
        self.entry_cidade['bg'] = '#00BFFF'
        self.entry_cidade['font'] = ('Arial 20')
        self.entry_cidade.grid(row=1,column=1)
#--------------------label_barrio e entry_barrio -----------------------------------------------------------
        self.label_barrio = Label(self.frame_05,padx=8)
        self.label_barrio['bd'] = 5
        self.label_barrio['bg'] = '#00BFFF'
        self.label_barrio['relief'] = RIDGE
        self.label_barrio['text'] = 'Barrio:'
        self.label_barrio['font'] = ('Arial 20')
        self.label_barrio.grid(row=2,column=0,sticky=W)

        self.entry_barrio = Entry(self.frame_05)
        self.entry_barrio['bd'] = 5
        self.entry_barrio['relief'] = SUNKEN
        self.entry_barrio['bg'] = '#00BFFF'
        self.entry_barrio['font'] = ('Arial 20')
        self.entry_barrio.grid(row=2,column=1)

#------------------- button ----------------------------------------------------
        self.btnA = Button(self.frame_11,text='INSERIR')
        self.btnA['bd'] = 5
        self.btnA['relief'] = SUNKEN
        self.btnA['bg'] = '#DAA520'
        self.btnA['font'] = ('Arial 15')
        self.btnA['command'] = self.exite
        self.btnA['width'] = 24
        self.btnA.grid(row=0,column=0)

        self.btnB = Button(self.frame_11,text='SAIR')
        self.btnB['bd'] = 5
        self.btnB['relief'] = SUNKEN
        self.btnB['bg'] = '#DAA520'
        self.btnB['font'] = ('Arial 15')
        self.btnB['command'] = self.sair
        self.btnB['width'] = 25
        self.btnB.grid(row=0,column=1)

        self.btnC = Button(self.frame_11,text='DELETA')
        self.btnC['bd'] = 5
        self.btnC['relief'] = SUNKEN
        self.btnC['bg'] = '#DAA520'
        self.btnC['font'] = ('Arial 15')
        self.btnC['command'] = self.delete
        self.btnC['width'] = 24
        self.btnC.grid(row=0,column=2)


#------------------- trieevem --------------------------------------------------
        self.triee = Treeview(self.frame_10,columns=('nome','cpf','fome','uf','cidade','barrio'),show='headings')
        self.triee.column('nome',width=170,)
        self.triee.column('cpf',width=100)
        self.triee.column('fome',width=148)
        self.triee.column('uf',width=100)
        self.triee.column('cidade',width=120)
        self.triee.column('barrio',width=198)


        self.triee.heading('nome',text='Nome')
        self.triee.heading('cpf',text='Cpf')
        self.triee.heading('fome',text='Fome')
        self.triee.heading('uf',text='Uf')
        self.triee.heading('cidade',text='Cidade')
        self.triee.heading('barrio',text='Barrio')
        self.triee.grid(row=0,column=0)



    def exite(self):
        if self.entry_nome.get() != '' and self.entry_cpf.get() != '' and self.entry_fome.get() != '' and self.entry_uf.get() != '' and self.entry_cidade.get() != '' and self.entry_barrio.get() != '':
            self.triee.insert("","end",values=(self.entry_nome.get(),self.entry_cpf.get()
                                               ,self.entry_fome.get(),self.entry_uf.get(),
                                                self.entry_cidade.get(),self.entry_barrio.get()))
            self.entry_nome.delete(0,END)
            self.entry_cpf.delete(0,END)
            self.entry_fome.delete(0,END)
            self.entry_uf.delete(0,END)
            self.entry_cidade.delete(0,END)
            self.entry_barrio.delete(0,END)
        else:
            messagebox.showinfo('','PREENCHAR O ESPACO')
    def sair(self):
        sim = messagebox.askyesno('','DESEJA SAIR ')
        if sim == True:
            root.destroy()

    def delete(self):
        try:
            apaga = self.triee.selection()[0]
            self.triee.delete(apaga)
        except :
            messagebox.showerror('ERRO !!!','SELECIONE UM ITEM ')

root = Tk()
Janelas(root)
root.geometry('900x540+200+100')
root.mainloop()