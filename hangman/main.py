import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

# Test Code
# print(f'The solution is {chosen_word}.\n')

bad_guesses = []
hangman_display = []
for _ in range(word_length):
    hangman_display += "_"
print(hangman_display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in hangman_display:
        print(f'You\'ve already successfully guessed the letter {guess}. Pick another.')

    for position in range(word_length):
        if chosen_word[position] == guess:
            hangman_display[position] = guess
        
    if guess not in chosen_word:
        lives -= 1
        bad_guesses += guess
        print(f'{guess} is not in the word. You have {lives} lives left.')
        if lives == 0:
            end_of_game = True

    print(hangman_display)
    
    if "_" not in hangman_display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])
    print(f"So far you've guessed these letters incorrectly: {bad_guesses}")

if end_of_game:
    print(f"You Lose! The word was {chosen_word}")
