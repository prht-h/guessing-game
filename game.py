import random 
num = random.randrange(1,101)
guessed = False

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.""")

print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")

difficulty = int(input(("Enter your choice: ")))

if difficulty == 1:
    i = 0
    while not guessed and i<10: 
        guess = int(input(("Enter your guess: ")))
        if guess == num:
            guessed = True
            print("Yes! The number is ", guess, ". You guessed it in ",i+1," attempts") 
        else:
            if num>guess:
                print("Incorrect! the number is greater than ", guess)
            else:
                print("Incorrect! the number is lesser than ", guess)
        i += 1

if difficulty == 2:
    i = 0
    while not guessed and i<5: 
        guess = int(input(("Enter your guess: ")))
        if guess == num:
            guessed = True
            print("Yes! The number is ", guess, ". You guessed it in ",i+1," attempts")
        else:
            if num>guess:
                print("Incorrect! the number is greater than ", guess)
            else:
                print("Incorrect! the number is lesser than ", guess)
        i += 1

if difficulty == 3:
    i = 0
    while not guessed and i<3: 
        guess = int(input(("Enter your guess: ")))
        if guess == num:
            guessed = True
            print("Yes! The number is ", guess, ". You guessed it in ",i+1," attempts") 
        else:
            if num>guess:
                print("Incorrect! the number is greater than ", guess)
            else:
                print("Incorrect! the number is lesser than ", guess)
        i += 1