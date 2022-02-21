#Random Exercise
mode = input("easy or hard mode????")
if mode == 'hard':
    import random
    number = random.randint(1,101)
else:
    import random
    number = random.randint(1,11)
count = 1
guess = int(input("What is the number????"))
while guess != number:
    if guess < number:
        print("Guess Higher")
        guess = int(input("What is the number????"))
        count = count+1
        if count == 10:
            print("too many Guessses, try again later")
            break
    elif guess > number:
        print("Guess lower")
        guess = int(input("What is the number????"))
        count = count+1
        if count == 10:
            print("too many Guessses, try again later")
            break
while guess == number:
    print("CORRECT")
    print(f"You took {count} guesses!!!!")
    break
