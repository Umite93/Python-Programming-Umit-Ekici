import random as rng

while True:
    number1 = rng.randint(1, 10)
    number2 = rng.randint(1, 10)

    user_answer = int(input(f"What is {number1} * {number2}?"))
    if user_answer == number1*number2:
        print("Correct!")
    else:
        print(f"{user_answer} is wrong!")

    play_again = input("Want to play again? (y for yes)")

    if play_again != "y":
        print("Good bye!")
        break