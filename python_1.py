import random
randnum = random.randint(1, 20)
name = input('Hi whats your name')
decision = input(name + ' do you want to play a game of guess the number')
if decision == 'yes':
    pass
else:
    print('Bye')

print('im thinking of a number between 0, 20')
numofguesses = 0

while numofguesses < 4:
    guess = input('guess a number')
    guess = int(guess)
    numofguesses = numofguesses + 1
    if guess < randnum:
        print('too low')
    elif guess > randnum:
        print('that was too high')
    else:
        break

if guess == randnum:
    print('winner, winner chicken dinner ' + name)
else:
    print('you lose the number was ' + str(randnum))
