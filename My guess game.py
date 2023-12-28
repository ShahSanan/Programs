import random
secret_number = random.randint(1, 100)
attempts = 5
while attempts > 0:
    #Input
    try:
        guess = int(input(f"Guess the number between 1 to 100. You have {attempts} attempts left: ")) 
    except ValueError:
        print("Invalid Input. Please enter Whole numbers")
        continue
    if guess == secret_number:
        print(f"Guess is correct. Absar, You gussed the number in {attempts} attempts. ")
        break
    else:
        attempts -= 1 
    
        if guess < secret_number:
            print("Your guess is low. Try again")
        else:
             print("Your guess is high. Try again")
            
if attempts == 0:
                    print(f"No more attempts left. the secret number was {secret_number} ")
                    print("Made by Sanan but with a little help from google.")

