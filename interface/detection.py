import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from datetime import datetime

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")  # Utiliser grid au lieu de pack
        self.create_widgets()

    def create_widgets(self):
        # Charger l'image
        image = Image.open("page 1.jpg")
        image = image.resize((800, 480))  # Ajuster la taille de l'image à la taille de l'écran
        self.photo = ImageTk.PhotoImage(image)
        self.background = tk.Label(self, image=self.photo)
        self.background.grid(row=0, column=0, sticky="nsew")  # Utiliser grid au lieu de place

        # Ajouter un formulaire de connexion
        self.username_label = tk.Label(self, text="Nom d'utilisateur", bg=self.master.cget('bg'), fg="midnight blue")  # Texte en bleu nuit
        self.username_label.place(relx=0.9, rely=0.9)  # Ajuster la valeur de rely
        self.username_entry = tk.Entry(self, font=('Arial', 14))  # Champ de texte plus grand
        self.username_entry.place(relx=0.5, rely=0.6)  # Ajuster la valeur de rely

        self.password_label = tk.Label(self, text="Mot de passe", bg=self.master.cget('bg'), fg="midnight blue")  # Texte en bleu nuit
        self.password_label.place(relx=0.4, rely=0.7)  # Ajuster la valeur de rely
        self.password_entry = tk.Entry(self, show="*", font=('Arial', 14))  # Champ de texte plus grand
        self.password_entry.place(relx=0.5, rely=0.7)  # Ajuster la valeur de rely

        self.login_button = tk.Button(self, text="Connexion", command=self.login, height=2, width=15, bg="#008000")  # Bouton plus grand et vert pickle
        self.login_button.place(relx=0.5, rely=0.8, anchor='center')  # Ajuster la valeur de rely

        # Ajouter la date
        self.date_label = tk.Label(self, text=datetime.now().strftime("%d/%m/%Y"), bg="white", fg="#008000")  # Texte en vert pickle
        self.date_label.place(relx=0.9, rely=0.05)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Vérifier les informations de connexion
        if username == "admin" and password == "123":  # Le mot de passe est maintenant "123"
            self.login_button.config(bg="#008000")  # Remettre la couleur du bouton en vert
            self.master.destroy()  # Fermer la fenêtre actuelle
            new_window = tk.Tk()  # Créer une nouvelle fenêtre
            new_window.title("Nouvelle Fenêtre")
            new_window.geometry("800x480")

            # Charger l'image pour la deuxième page
            image2 = Image.open("page 2.jpg")
            image2 = image2.resize((800, 480))  # Ajuster la taille de l'image à la taille de l'écran
            self.photo2 = ImageTk.PhotoImage(image2)
            background2 = tk.Label(new_window, image=self.photo2)
            background2.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            print("Nom d'utilisateur ou mot de passe incorrect")
            self.login_button.config(bg="red")  # Changer la couleur du bouton en rouge

root = tk.Tk()
root.geometry("800x480")  # Définir la taille de la fenêtre
root.minsize(800, 480)  # Définir la taille minimale de la fenêtre
root.maxsize(800, 480)  # Définir la taille maximale de la fenêtre
root.grid_rowconfigure(0, weight=1)  # Permettre au widget de la rangée 0 de s'étendre lorsque la fenêtre est redimensionnée
root.grid_columnconfigure(0, weight=1)  # Permettre au widget de la colonne 0 de s'étendre lorsque la fenêtre est redimensionnée
app = HomePage(master=root)
app.mainloop()
