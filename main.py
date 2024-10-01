import random
import ipywidgets as widgets
from IPython.display import display


words = ['apple', 'banana', 'orange', 'mango', 'strawberry']


word_hints = {
    'apple': "It is a delicious fruit.",
    'banana': "It is a tropical fruit.",
    'orange': "It is rich in vitamin C.",
    'mango': "It is often used in desserts.",
    'strawberry': "It is a popular smoothie ingredient."
}


def update_display():
    guessed_word_label.value = ' '.join(guessed_word)
    attempts_left_label.value = f'Attempts Left: {attempts_left}'


def check_game_over():
    if '_' not in guessed_word:
        print('Congratulations! You won the game!')
        new_game_button.disabled = False
        guess_button.disabled = True
        hint_button.disabled = True
    elif attempts_left == 0:
        print(f'Game Over. The word was: {secret_word}')
        new_game_button.disabled = False
        guess_button.disabled = True
        hint_button.disabled = True


def give_hint(button):
    global guessed_word, words, word_hints
    sentence = word_hints.get(secret_word, "No hint available.")
    print(f"Sentence Hint: {sentence}")
    update_display()


def guess_letter(button):
    global attempts_left
    letter = letter_entry.value
    letter_entry.value = ""
    
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed_word[i] = letter
    else:
        attempts_left -= 1
    
    update_display()
    check_game_over()


def new_game(button):
    global secret_word, guessed_word, attempts_left
    secret_word = random.choice(words)
    guessed_word = ['_'] * len(secret_word)
    attempts_left = 5
    update_display()


guessed_word_label = widgets.Label(value='')
attempts_left_label = widgets.Label(value='')
letter_label = widgets.Label(value='Guess a letter:')
letter_entry = widgets.Text(value='')

guess_button = widgets.Button(description='Guess')
new_game_button = widgets.Button(description='New Game')
hint_button = widgets.Button(description='Hint')


guess_button.on_click(guess_letter)
new_game_button.on_click(new_game)
hint_button.on_click(give_hint)


display(guessed_word_label)
display(attempts_left_label)
display(letter_label)
display(letter_entry)
display(guess_button)
display(new_game_button)
display(hint_button)


new_game(new_game_button)
