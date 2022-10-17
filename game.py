import random

computer_score = 0
user_score = 0

options = ['rock','paper','scissors']

while True:
    user_choice = input('Pick on of (rock, paper, scissors ):\n  ')
    computer_choice = random.choice(options)

    if user_choice == 'rock':
        if computer_choice == 'rock':
            print(f'Computer choose {computer_choice}')
            print("It's a draw.")
        elif computer_choice == 'paper':
            print(f'Computer choose {computer_choice}')
            print("Computer won. LOSER!")
            computer_score += 1
        elif computer_choice == 'scissors':
            print(f'Computer choose {computer_choice}')
            print('Congrats!!! U have won!!!')
            user_score += 1

    elif user_choice == 'paper':
        if computer_choice == 'paper':
            print(f'Computer choose {computer_choice}')
            print("It's a draw.")
        elif computer_choice == 'scissors':
            print(f'Computer choose {computer_choice}')
            print("Computer won. LOSER!")
            computer_score += 1
        elif computer_choice == 'rock':
            print(f'Computer choose {computer_choice}')
            print('Congrats!!! U have won!!!')
            user_score += 1

    elif user_choice == 'scissors':
        if computer_choice == 'scissors':
            print(f'Computer choose {computer_choice}')
            print("It's a draw.")
        elif computer_choice == 'rock':
            print(f'Computer choose {computer_choice}')
            print("Computer won. LOSER!")
            computer_score += 1
        elif computer_choice == 'paper':
            print(f'Computer choose {computer_choice}')
            print('Congrats!!! U have won!!!')
            user_score += 1

    print(f'Computer score is: {computer_score}')
    print(f' User score is: {user_score}')
    end_game = input("Do u want to end game ? y/n \n: ")
    if end_game == 'y':
        print('Thanks for the game. ')
        if user_score > computer_score:
            print('U have won this competition. Congratulations!')
        elif user_score == computer_score:
            print("It's a draw of this competition")
        elif user_score < computer_score:
            print('U have lost this competition. ')
        break
    else:
        pass