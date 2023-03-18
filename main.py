import random

number = random.randint(1, 100)
guesses = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    guesses += 1
    
    if guess == number:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
