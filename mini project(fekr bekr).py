#this library helps us to make random numbers.
#in this program helps us to make password.(secret password)
import random

def make_password():
    """
    this function help us 
    to make password for game
    with different digits.
    """
    password=[]
    while len(password)<4 :
        num=random.randint(1,6)
        if num not in password:
            password.append(num)

    return password

def check_input(guess):
    """
    This function check the validity of the user's guess.
    """
    if len(guess) != 4 :
        return False
    for i in range(len(guess)):
        if (guess[i]) < "1" or (guess[i]) > "6" :
            return False

    for i in range(len(guess)):
        for j in range (i+1 , len(guess)):
            if guess[i]==guess[j]:
                return False

    return True


def receive_guess():
    """
    This function receives the user's guess
    and check if it follows the rules of game.
    """
    while True:
        guess=input("Enter your guess and try your chance!:\n")

        if check_input(guess):
            return guess

        else:
            print("Try again!")


def compare_geuss_vs_password(password,guess):
    """
    This function compare user's guess with secret password,
    count digits that are in the correct place.
    also count all common digits between the guess and password.
    at the end calculates the digits that are correct but in the wrong place.
    """
    correct_digit_correct_place=0
    total_digit=0

    for i in range(4):
        if int(guess[i]) == int(password[i]):
            correct_digit_correct_place+=1

        for j in range (4):
            if int(guess[i]) == int(password[j]):
                total_digit+=1

    wrong_place =  total_digit - correct_digit_correct_place

    return correct_digit_correct_place , wrong_place


def start_game():
    """
    This function start the game 
    -show informations of game
    -make password
    -generate password and user's guess 
    -check the rules of each guess
    -show result of game
    """

    print("Name of game:'Fekr bekr'")
    print("Name of programmer: Fatemeh Rahimi")
    print("----------------------------------")

    password=make_password()

    #user just has 10 chance to try it.
    chance=10
    win=False

    while chance>0:
        print(f"Remain of your chance: {chance}")
        guess=receive_guess()

        chance-=1

        correct , wrong = compare_geuss_vs_password(password,guess)

        print(f"Correct digits in correct place: {correct}")
        print(f"Correct digits in wrong place: {wrong}")

        if correct == 4 :
            win = True

            print("Perfect you won.")
            print(f"Number of your trying:{10-chance}")

            break

    if win == False :
        print("Sorry you lost.")
        print("Real password:",end="")
        
        for i in password:
            print(i,end="")

#start_game
start_game()
