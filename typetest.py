import random 
import time
import requests


def typing():

    r = requests.get("https://gist.githubusercontent.com/ga-vlach/02181e88f175bce3f54fb1211b2a9374/raw/c36a15492d403e8f42423aa324013b882030b34b/gistfile1.txt")

    while True:

                l = list(range(1000))
                random.shuffle(l)

                data = r.text

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

                input("Press enter to start typing whenever you're ready.\n")
                
                text.split()
                print(f"{text}\n")
                

                start_time = time.time()
                
                user = input()
                user = list(user.split())
                
                j = 0
                for i in range(len(user)):
                    
                    if text_list[i] != user[j]:

                        user.pop(j)

                    else:
                        j+=1

                end_time = time.time()

                #Calculating the gross wpm
                g_typing_speed = len(text_list) / ((end_time - start_time) / 60)

                #Calculating net wpm, user is the correct words only
                n_typing_speed = len(user) / ((end_time - start_time) / 60)

                #Calculating the accuracy
                accuracy = (n_typing_speed * 100) / g_typing_speed

                print(f"Your net typing speed is {n_typing_speed:.2f} words per minute!")
                print(f"\nYour raw typing speed is {g_typing_speed:.2f} words per minute!\n")
                print(f"{accuracy:.2f}% accuracy")


                while True:

                    again = str(input("\n\nDo you want to play again? "))

                    again = again.lower()
                
                    if again == "no":
                        return 0
                    elif again == "yes":
                        break
                    else:
                        print("\nInvalid answer")


typing()
