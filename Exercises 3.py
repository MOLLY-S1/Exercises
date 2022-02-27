#Random Exercise
mode = input("easy or hard mode????")
mode = mode.upper()
if mode == 'HARD':
    import random
    number = random.randint(1,101)
    count = 1
guess = int(input("What is the number????"))
while guess != number:
    if guess < number:
        print("Guess Higher")
        guess = int(input("What is the number????"))
        count = count+1
        if count == 4:
            print("too many Guessses, try again later")
            print(f"the number was {number}")
            break
    elif guess > number:
        print("Guess lower")
        guess = int(input("What is the number????"))
        count = count +1
        if count == 4:
            print("too many Guessses, try again later")
            print(f"the number was {number}")
            break
while guess == number:
    print("CORRECT")
    print(f"You took {count} guesses!!!!")
    break
else:
    import random
    number = random.randint(1,101)
count = 1
guess = int(input("What is the number????"))
while guess != number:
    if guess < number:
        print("Guess Higher")
        guess = int(input("What is the number????"))
        count = count+1
        if count == 10:
            print("too many Guessses, try again later")
            print(f"the number was {number}")
            break
    elif guess > number:
        print("Guess lower")
        guess = int(input("What is the number????"))
        count = count+1
        if count == 10:
            print("too many Guessses, try again later")
            print(f"the number was {number}")
            break
while guess == number:
    print("CORRECT")
    print(f"You took {count} guesses!!!!")
    break
