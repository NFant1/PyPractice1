#Creating Python functions
#Taking user input, call functions to determine user's favorite fruit
#Figured out how to push to github fromm VS code!
#git remote add origin link
#git push -u origin main

response  = input("What is your favorite color?")

def user_input(response):
    if(response == "red"):
        print("You love Apples!")
    elif(response == "orange"):
        print("You love Oranges!")   
    elif(response == "pink"):
        print("You love Dragon Fruit!")
    elif(response == "yellow"):
        print("You love Lemons!")
    elif(response == "blue"):
        print("You love Blueberries!")
    elif(response == "purple"):
        print("You love Raspberries!")

user_input(response)