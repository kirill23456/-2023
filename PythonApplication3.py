import random

def get_word_from_user():
    # Функція для отримання слова та його опису від користувача
    word = input("Введіть слово: ").lower()
    description = input("Введіть опис для слова: ")
    return word, description

def display_state(word, guessed_letters):
    # Функція для відображення поточного стану слова з відгаданими літерами
    current_state = ""
    for letter in word:
        if letter in guessed_letters:
            current_state += letter + " "
        else:
            current_state += "_ "
    return "Поточний стан: " + current_state

def make_guess():
    # Функція для отримання відгадки літери від користувача
    guess = input("Вгадайте літеру: ").lower()
    return guess

def play_hangman():
    # Функція для гри в гру "Висілок"
    word, description = get_word_from_user()
    guessed_letters = []
    attempts = 9

    print("Ласкаво просимо до гри 'Шибеницю'!")
    print("Опис:", description)

    while attempts > 0:
        print(display_state(word, guessed_letters))
        guess = make_guess()

        if guess == word:
            print("Вітаємо! Ви вгадали слово:", word)
            break

        if set(guess) == set(word):
            print("Вітаємо! Ви вгадали слово:", word)
            break

        if guess in guessed_letters:
            print("Ви вже вгадали цю літеру. Спробуйте ще раз.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Неправильна відгадка! У вас залишилося {attempts} спроб.")

    if attempts == 0:
        print("Вибачте, у вас закінчилися спроби. Правильне слово було:", word)

if __name__ == "__main__":
    play_hangman()



















 


















        


