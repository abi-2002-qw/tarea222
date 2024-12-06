#vanessa abigail alvardo elizalde #
#adivinar el numero :) #
# numero disponible del ( 1 al 10 ) 
#
##
# agregar una inferfaz grafica ###


import tkinter as tk
from tkinter import messagebox
import random



class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("adivina el número")
        self.target_number = random.randint(1, 10)#1-10#
        self.attempts_left = 10
        
        self.label = tk.Label(root, text="Adivina entre 1 y 10")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Adivinar", command=self.check_guess)
        self.guess_button.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.attempts_label = tk.Label(root, text=f"Intentos restantes: {self.attempts_left}")
        self.attempts_label.pack()

        self.reset_button = tk.Button(root, text="Reiniciar", command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 10: #1-10#
                self.feedback_label.config(text="Por favor, ingresa un número entre 1 y 10.")
                return

            self.attempts_left -= 1
            self.attempts_label.config(text=f"Intentos restantes: {self.attempts_left}")
            #vamos a utilizar la funcion if y elif#
            if guess == self.target_number:
                self.feedback_label.config(text="¡Correcto! Has adivinado el número.")
                messagebox.showinfo("¡Felicidades!", "Has adivinado el número correctamente.")
                self.reset_game()
            elif guess < self.target_number:
                self.feedback_label.config(text="Demasiado bajo. Intenta con un número más alto.")
            else:#else
                self.feedback_label.config(text="Demasiado alto. Intenta con un número más bajo.")
            
            if self.attempts_left == 0:
                messagebox.showinfo("Fin del Juego", f"Has perdido. El número correcto era {self.target_number}.")
                self.reset_game()
        
        except ValueError:
            self.feedback_label.config(text="Por favor, ingresa un número válido.")

    def reset_game(self):
        self.target_number = random.randint(1, 10)
        self.attempts_left = 10
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.attempts_label.config(text=f"Intentos restantes: {self.attempts_left}")








if __name__ == "__main__":
    root = tk.Tk()
    # con esto estamos crear la ventana principal de la aplicación

    game = NumberGuessingGame(root)
    # juego  adivinar la ventana principal
    root.mainloop()
    # iniciar el bucle de eventos de Tkinter

