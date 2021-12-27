# HANGMAN GAME


# ran=random.choices(['a','s','d'],['f','g'])
# print(ran)
# p=(input("write a word: "))
# print(lives_visual_dict[lives])
# # if ran==p:
# #     print("yoyo")
# word =["yoyo","afd"]
# if __name__ == '__main__':
from hangman_visual import lives_visual_dict
import random
from word import word 
import string

def get_valid_word(word):
    words=random.choice(word)
    while '-' in words :
        words=random.choice(word)
    return words.upper()


def hangman():
    words=get_valid_word(word)
    word_letter=set(words)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives =7
     
    while len(word_letter)>0 and lives>0:
        print(f"You have {lives} left and you have used these letters {' '.join(used_letters)} :)")
        word_list=[letter if letter in used_letters else '_' for letter in words ]
        print(lives_visual_dict[lives])
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print('')
            else:
                lives = lives - 1  
                print(f'\nYour letter, {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', words)
    else:
        print('YAY! You guessed the word', words, '!!')



hangman()

