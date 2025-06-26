import random 
import time
import requests
import os


class typeTest():


    def createfile(file):
        for file in os.listdir():

            if file != "typetestwords.txt": #If file doesn't exist, creates new file

                try: 
                    file = open("typetestwords.txt", "x")
                
                except FileExistsError: #If file exists, stops the for loop
                    break

                else: #Takes the text from the gist file and writes it into typetestwords.txt
            
                    r = requests.get("https://gist.githubusercontent.com/ga-vlach/02181e88f175bce3f54fb1211b2a9374/raw/c36a15492d403e8f42423aa324013b882030b34b/gistfile1.txt")

                    with open("typetestwords.txt" , "a") as file:

                        file.write(r.text)


    def typing(test):

        while True:
                    #makes a list of numbers ranging from 0-999 and shuffles it
                    l = list(range(1000))
                    random.shuffle(l)

                    f = open("typetestwords.txt" , "r") #opens file
                    data = f.read() #reads contents of file

                    words = data.split() #splits each word into a list

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

                        text += words[chosen_word] + ' ' #adds all the words that will be displayed into a list, also adds a sapce between each one
                        text_list.append(words[chosen_word])
                        j+=1

                    input("Press enter to start typing whenever you're ready.\n")
                    
                    print(f"{text}\n")
                    

                    start_time = time.time()
                    
                    user = input()
                    user = list(user.split()) #adds each word the user wrote into a list

                    k = 0
                    correct_words = []
                    #creates a seperate list from the user input, ignores excess words
                    for word in range(len(user)):

                        if k < len(text_list):

                            correct_words.append(user[word])
                        else:
                            break
                        k+=1
                    
                    #deletes each incorrect word from the list
                    j = 0
                    for i in range(len(correct_words)): 
                        
                        if text_list[i] != correct_words[j]:

                            correct_words.pop(j) 
                        else:

                            j+=1

                    end_time = time.time()

                    #Calculating the gross wpm
                    g_typing_speed = len(text_list) / ((end_time - start_time) / 60)

                    #Calculating net wpm, user is the correct words only
                    n_typing_speed = len(correct_words) / ((end_time - start_time) / 60)

                    #Calculating the accuracy
                    accuracy = (n_typing_speed * 100) / g_typing_speed

                    print(f"Your net typing speed is {n_typing_speed:.2f} words per minute!")
                    print(f"\nYour raw typing speed is {g_typing_speed:.2f} words per minute!\n")
                    print(f"{accuracy:.2f}% accuracy")


                    while True:

                        again = str(input("\n\nDo you want to play again? "))

                        again = again.lower() #takes user input and converts it to lowercase, so it isn't case sensitive
                    
                        if again == "no":
                            return 0
                        elif again == "yes":
                            break
                        else:
                            print("\nInvalid answer")


typer = typeTest()
typer.createfile()
typer.typing()