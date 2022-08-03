import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blank_word = ""
while word_length > 0:
    blank_word += "_"
    word_length -= 1
print(blank_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter:\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print(letter)
    else:
        print("_")

print("Yay! 😀 ")