import random
import art
import words

print(art.logo)

chosen_word = random.choice(words.word_list)
display = []
number_of_tries = 6

print(art.stages[len(art.stages)-1])

for _ in chosen_word:
    display.append("_")
print(display)

already_guessed_letters = []

while "_" in display and number_of_tries > 0:
    guess = input("Insert letter: ").lower()
    if guess in already_guessed_letters:
        print("You already suggested this letter.")
    else:
        letter_found = False
        for index in range(len(chosen_word)):
            if guess == chosen_word[index]:
                display[index] = guess
                letter_found = True
        if not letter_found:
            number_of_tries -= 1
            print(art.stages[number_of_tries])
        print(display)
    already_guessed_letters.append(guess)


if number_of_tries > 0:
    print("You won!")
else:
    print("You lose.")
