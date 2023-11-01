import random
import art
import word_list


print(art.hangman_logo[0] + art.hangman_logo[1])

chosen_word = random.choice(word_list.word_list).lower()
hangman_step = 0
display = []
chosen_letters = []
hangman_pics = art.hangman_pics

for letter in chosen_word:
    display.append('_')

while hangman_step < len(hangman_pics) - 1 and '_' in display:
    guess = input("Guess a letter: ").lower()

    chosen_letters.append(guess)

    while not (guess.isalpha() and len(guess) == 1):
        print("Please enter a valid letter.")
        guess = input("Guess a letter: ").lower()

    if guess in display:
        print('Choose another letter')
    else:

        for index, letter in enumerate(chosen_word):
            if guess == letter.lower():
                display[index] = letter

        if guess not in display:
            hangman_step += 1

        print(' '.join(display))
        print(hangman_pics[hangman_step])
        print(f'Already chosen letters are: {' '.join(chosen_letters)}')

if '_' not in display:
    print(f'You win!. Chosen word: {chosen_word}')

if hangman_step == len(hangman_pics) - 1:
    print(f"You lose. The chosen word was: {chosen_word}")
