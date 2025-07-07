# 1. Import random module
import random

# 2. Define a function to generate a random number
def generate_random():
    return random.randint(1, 100)

# 3. Define main function
def main():
    number = generate_random()
    attempts = 0
    print("Guess the number between 1 and 100")

    # 4. Loop until correct guess
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        # 5. Check conditions
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! Attempts: {attempts}")
            break

# 6. Run main
if __name__ == "__main__":
    main()
