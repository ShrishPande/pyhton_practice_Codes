import random
n =random.randint(1,100)
print("You have total 9 guesses")

no_of_guesses =9

while no_of_guesses>=1:
    no_of_guesses-=1
    x= int(input("Enter Your Guess\n"))
    if x<n:
        print("Your number is too less!")
        print(f'you have {no_of_guesses} guesses left')
    elif x>n:
        print("Your number is too high!")
        print(f'you have {no_of_guesses} guesses left')
    else :
        print(f"You have guessed the right number in {9-no_of_guesses} guesses\nYou Won!")
        break

    if no_of_guesses == 0:
        print("Game Over!")
    
    
