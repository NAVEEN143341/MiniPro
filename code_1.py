import random


def number_guessing_game():
    x = int(input("Enter lower bound: "))
    y = int(input("Enter upper bound: "))


    number_to_guess = random.randint(x, y)
    attempts = 0


    while True:
        user_guess = int(input(f"Guess a number ({x} to {y}): "))
        attempts += 1


        if user_guess == number_to_guess:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
        number_guessing_game()


if __name__ == "__main__":
    number_guessing_game()
