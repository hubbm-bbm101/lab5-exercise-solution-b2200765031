import random
hidden = random.randint(10,100)
user_guess = int(input("Please guess the number I picked between 10 and 100: "))
while hidden !=user_guess:
    if hidden < user_guess:
        user_guess = int(input("Please decrease your number!"))
    else:
        user_guess = int(input("Please increase your number!"))

print("Congratulations ! ")
