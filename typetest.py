import random 
import time
import sys


def typing():

    with open("words.txt", 'r') as file:

        l = list(range(100))
        random.shuffle(l)

        data = file.read()
        words = data.split()

        text = ''
        text_list = []

        while True:
            
            try:
                count = int(input("How many words do you want to type?\n"))

            except:
                print("\nEnter an integer please")
            
            else:
                break
        
        j = 0
        #Choosing random words from the document
        for i in range(count):

            chosen_word = l[j]

            text += words[chosen_word] + ' '
            text_list.append(words[chosen_word])
            j+=1

        text.split()
        
        print(text)
        
        start_time = time.time()
        
        correct_words = []
        i = 0
        j = 0
        
        #Taking the correct input

        for line in sys.stdin:
            #Clears every input
            print("\033[A                             \033[A")

            correct_words.append(line.rstrip())
            
            if text_list[i] != correct_words[j]:
                correct_words.pop(j)
            
            else:
                j+=1

            if i == len(text_list) - 1:
                break
            i+=1


        end_time = time.time()

        #Calculating the gross wpm
        g_typing_speed = len(text_list) / ((end_time - start_time) / 60)

        #Calculating net wpm
        n_typing_speed = len(correct_words) / ((end_time - start_time) / 60)

        #Calculating the accuracy
        accuracy = (n_typing_speed * 100) / g_typing_speed

        print(f"Your net typing speed is {n_typing_speed:.2f} words per minute!")
        print(f"\nYour raw typing speed is {g_typing_speed:.2f} words per minute!\n")
        print(f"{accuracy:.2f}% accuracy")


typing()
