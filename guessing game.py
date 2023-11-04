def guessing_game():
    guess_attempt = 0
    guess_limit = 3
    secret_number = 87

    while guess_attempt < guess_limit:
        guess = int(input("Guess: "))
        guess_attempt += 1
        if guess == secret_number:
            print('you win')
        break
    else:
        print('you lose')
    

guessing_game()
        
    

        

