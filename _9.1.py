import random

def guess_the_number():
    """
    A number guessing game where the user has 10 attempts to guess a randomly generated number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the number guessing game! 🎲")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt #{attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        
        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts! 🎉")
            return

    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The number I was thinking of was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
