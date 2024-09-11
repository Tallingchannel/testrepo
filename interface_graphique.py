from tkinter import *
import webbrowser

def ouvrir_youtube  () :
    webbrowser.open_new('https://youtube.com/')

#creer fenetre principale
fenetre_1 = Tk()

#modifier les caracteristiques de la fenetre 
fenetre_1.title ("ma premiere fenetre")
fenetre_1.geometry ("1080x300")
fenetre_1.minsize(650, 350)
fenetre_1.iconbitmap ("E:\mes programmes\Tests python\phoque.ico")
fenetre_1.config(background = '#33FFA3')

#creation d'une boite pour contenir les elements de la fenetre 
boite_1 = Frame (fenetre_1, bg='#33FFA3', bd=1, relief= 'groove')

#ajout du premier composant de la fenetre
titre_1 = Label (boite_1, text = 'Bienvenue sur Queenchama Services', bg = '#33FFA3', font= ('Verdana', 20), fg = 'white')
#titre_1.pack(side='bottom')
titre_1.pack()

#ajout du premier composant de la fenetre
titre_2= Label (boite_1, text='Je suis Channel, votre guide!', font=('Arial', 18), bg = '#33FFA3', fg= 'gray')
titre_2.pack()

#ajout bouton de redirection
btn_1 = Button (boite_1, text= 'Ouvrir Youtube', bg = 'skyblue', font = 10, fg= 'black', pady= 8, padx=10, command=ouvrir_youtube)
btn_1.pack(pady=15)

#affichage de la boite dans la fenetre
boite_1.pack(expand=YES)

# afficher fenetre principale
fenetre_1.mainloop()