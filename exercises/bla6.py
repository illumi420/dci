import random

secret_number = random.randint(0,99)
guessed_number = random.randint(0,99)
false_tries = ""
tries = 1

while secret_number != guessed_number:
    print(guessed_number,"is not secret number")
    # storing wrong guesses to prevent using them again
    false_tries += str(guessed_number)
    # counting the number of loops it took to break out
    tries += 1
    # guess again
    guessed_number = random.randint(0,99)
    # check if new guess was given before
    if str(guessed_number) in false_tries:
        # guess was made before therefore should be not counted again as try
        tries -= 1
        guessed_number = random.randint(0,99)
    else:
        pass

print(f"Loop is Broken, the secret number {secret_number} is found, after {tries} tries.")    



