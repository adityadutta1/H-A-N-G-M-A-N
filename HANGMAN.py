# H-A-N-G-M-A-N GAME created by @devb113#
import random
from collections import Counter

print("""H A N G M A N""")
for i in range(100):  # loop used for  asking user whether they  wants to play again "H A N G M A N" game or not
    name=input('enter your name')
    print('Hello')
    print(name)
    again = input('Type "play" to play the game, "exit" to quit:')
    if again == "play":  # set the limit_1 to 8 so that user gets 8 chances
        limit_1 = 8

        print("")
        count = 0
        list_1 = ['python', 'java', 'kotlin', 'javascript']  # random function is used to select a word from this list
        a = random.choice(list_1)
        extra = len(a)
        letter = str("-") * extra  # converting random word into "-" form
        i = 1
        arr = []  # empty array used for storing all inputs given by user
        count_1 = 1

        while limit_1 != 0:  # run until chances is reduce to 0
            print(letter)
            num = input("Input a letter:")
            arr.append(num)  # adding user input to empty array
            val = arr.count(num)  # count the number of times a variable in occur in array
            size = len(num)
            if size > 1 or size == 0:  # if input have 2 or more characters
                print("You should input a single letter")
                print("")

            if not num.islower() and size == 1:  # input is in lowercase and only one character
                print("It is not an ASCII lowercase letter")
                print("")

            if num in letter or val > 1:  # input is already used before
                print("You already typed this letter")

                if a != letter:
                    print('')

            if num not in a and num.islower() and size == 1 and val == 1:   # not satisfying previous conditions
                limit_1 = limit_1 - 1
                print('No such letter in the word')
                 print(' think wisely')
                
                if a != letter and limit_1 != 0:
                    print("You still have few chances left ")

            if limit_1 == 0 and a != letter:    # you are not able to guess the right word
                # print("")
                print('''You are hanged!''')
                print("")
                break

            if num in a and num not in letter:    # if input character is more than 1 time's in unknown word

                count_1 += 1
                count = Counter(a)
                times = count[num]

                b = a.index(num)

                letter = letter[0:b] + num + letter[b + 1:]
                if times == 1:
                    if limit_1 != 0 and a != letter:
                        # print(letter)
                        print("")

                if times == 2:
                    b = a.index(num, b + 1)
                    letter = letter[0:b] + num + letter[b + 1:]
                    if limit_1 != 0 and a != letter:
                        # print(letter)
                        print("")

                if a == letter:        # you guess the right word before losing all chances
                    # print("")
                    print(f'You guessed the word {a}')
                    print('CoNgRaTs you survived')
                    print('You survived!')
                    print("")
                    break

    if again == "exit":  # exit out of the "H A N G M A N" game if user input "exit"
        break
