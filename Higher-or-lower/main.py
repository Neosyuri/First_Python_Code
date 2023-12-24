import random

from game_data import data

from art import logo
from art import vs

x = len(data)

print(logo)

# CREAR FRASES

def string_creation():
    rnd_num = random.randint(0, x - 1)
    selection = data[rnd_num]
    selection_value = selection.get('follower_count')
    return selection

a_person = string_creation()
b_person = string_creation()

# COMPARAR OPCIONES

def compare_option(a, b):
    a_description = print(f"Compare A: {a.get('name')} a {a.get('description')} from {a.get('country')}")
    a_score = a.get('follower_count')
    print(a_score)

    print(vs)

    b_description = print(f"Against B: {b.get('name')} a {b.get('description')} from {b.get('country')}")
    b_score = b.get('follower_count')
    print(b_score)

    if a_score > b_score:
        winner = a
    else:
        winner = b

    decision = input("Who has more followers? 'A' or 'B'")
    t_or_f = decision == 'a' and a_score > b_score or decision == 'b' and b_score > a_score
    if t_or_f:
        print("Correct")
        a = winner
        b = string_creation()
        compare_option(a, b)
    else:
        print("You lost")
        rematch = input("Would you like to play again? 'Y' or 'N'")
        if rematch == 'y':
            a_person = string_creation()
            b_person = string_creation()
            compare_option(a_person, b_person)
        else:
            print("Goodbye")







compare_option(a_person, b_person)







