import random



print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("What difficulty, type 'easy' or 'hard': ")
diff = True
try_left = 0

if difficulty == "easy":
    print("You have 10 chance to guess the number")
elif difficulty == "hard":
    diff = False
    print("You have 5 chance to guess the number")

def new_game():
    continue_play = input("Would you like to play another time? Type 'yes' or 'no':")
    if continue_play == "yes":
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
        game()
    if continue_play == "no":
        return print("Thanks for playing")
def game():
    secret_number = random.randint(1, 100)
    n = secret_number
    print(f"Pssst, the secret number is {n} ")
    global try_left
    if diff:
        try_left = 10
    else:
        try_left = 5
    while try_left > 0:
        user_number = int(input("What is your number"))
        if user_number == n:
            print(f"Correct, you win the secret number was {n}")
            try_left = 0
            return new_game()
        elif user_number < n:
            print("Too low")
            try_left -= 1
            print(f"Try Again, you have {try_left} chances")
        elif user_number > n:
            print("Too high")
            try_left -= 1
            print(f"Try Again, you have {try_left} chances")
        else:
            print("You lose")
            try_left = 0
            return new_game()



game()
new_game()
