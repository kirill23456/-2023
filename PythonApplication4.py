from random import choice
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

def show_win_message():
    win_message = "Вітаю, ви виграли!"
    messagebox.showinfo("Перемога", win_message)

def show_loss_message():
    loss_message = "Ви програли. Спробуйте ще раз!"
    messagebox.showinfo("Тебе повісили", loss_message)

max_wrong = len(HANGMAN) - 1
WORDS = ("python", "ігра", "книга", "стіл", "гроші")  # Слова для вгадування

word = choice(WORDS)  # Слово, яке потрібно вгадати

so_far = "_" * len(word)  # Одна _ для каждої літери в слові, яке потрібно вгадати
wrong = 0  # Кількість невірних припущень, зроблених гравцем
used = []  # Літери вже вгадані

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])  # Виведення шибеника за індексом
    print("\nВи використали наступні літери:\n", used)
    print("\nНа данний момемнт слова виглядають так:\n", so_far)
    guess = input("\nВведіть літеру\n: ")  # Користувач вводить передбачувану літеру 
    while guess in used:
        print("Ви вже вводили цю літеру", guess)  
        guess = input("Введіть своє припущення: ")       
                 
    used.append(guess)  # В список використаних літер додається введена літера
    
    if guess == word: # Перевіряє чи введене ціле слово є загаданим словом
        break
    elif guess in word:  # Якщо введена літера є в загаданому слові, виводимо повідомлення
        print("Так!", guess, "є в слові!")
        new = ""
        for i in range(len(word)):  #У циклі додаємо знайдену букву в потрібне місце
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nвибачте, літери \"" + guess + "\" немає в слові.")  # Якщо літери немає, то виводимо повідомлення про це
        wrong += 1
        
if wrong == max_wrong:  # Якщо гравець перевищив кількість помилок, то його повісили
    print(HANGMAN[wrong])
    show_loss_message()
    print("\nЗагадене слово було \"" + word + '\"')
else: # Якщо кількість помилок не перевищена, то гравець переміг
    show_win_message()

    
print("\nЗагадене слово було \"" + word + '\"')




   


