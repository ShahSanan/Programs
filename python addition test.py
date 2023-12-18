import random

attempts = 1

while attempts < 2:
    digit_type = input("Choose a difficulty: single digit, double digit, or triple digit: ")

    if digit_type == "single digit":
        for _ in range(10):
            number1 = random.randint(1, 9)
            number2 = random.randint(1, 9)
            sum = number1 + number2
            answer = int(input(f"{number1} + {number2} = "))
            if answer != sum:
                print("Incorrect. Go back to nursery!")
                attempts += 1
                break
            else:
                print(f"{number1} + {number2} = {answer} (Correct)")

    elif digit_type == "double digit":
        for _ in range(10):
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
            sum = number1 + number2
            answer = int(input(f"{number1} + {number2} = "))
            if answer != sum:
                print("Incorrect. Try again!")
                attempts += 1
                break
            else:
                print(f"{number1} + {number2} = {answer} (Correct)")

    elif digit_type == "triple digit":
        for _ in range(10):
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)
            sum = number1 + number2
            answer = int(input(f"{number1} + {number2} = "))
            if answer != sum:
                print("Incorrect. Try again!")
                attempts += 1
                break
            else:
                print(f"{number1} + {number2} = {answer} (Correct)")

if attempts == 2:
    print("You have run out of attempts.")

