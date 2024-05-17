#Emma Brady

# Create a rock-paper-scissors game!
# - Play once and report the result

from numpy import random

choices = ['rock', 'paper', 'scissors']

# Get player 1's choice
p1 = input('Pick one of rock, paper, or scissors: ').lower()

# Validate player 1's choice
if p1 not in choices:
    print('Invalid choice. Please pick either rock, paper, or scissors.')
else:
    # Get player 2's choice (computer choice)
    p2 = random.choice(choices)

    print(f'Player 1 chose: {p1}')
    print(f'Player 2 chose: {p2}')

    # Determine the winner
    if p1 == p2:
        print("It's a tie!")
    elif (p1 == 'rock' and p2 == 'scissors') or \
         (p1 == 'scissors' and p2 == 'paper') or \
         (p1 == 'paper' and p2 == 'rock'):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
        
#player 2 wins

# - Play in a loop and record how many wins and losses happen?

choices = ['rock', 'paper', 'scissors']

wins = 0
losses = 0

num_rounds = int(input("How many rounds do you want to play? "))

for _ in range(num_rounds):
    p1 = input('Pick one of rock, paper, or scissors (or type "quit" to end): ').lower()

    if p1 == 'quit':
        break

    if p1 not in choices:
        print('Invalid choice. Please pick either rock, paper, or scissors.')
        continue

    p2 = random.choice(choices)
    print(f'Player 1 chose: {p1}')
    print(f'Player 2 chose: {p2}')

    if p1 == p2:
        print("It's a tie!")
    elif (p1 == 'rock' and p2 == 'scissors') or \
         (p1 == 'scissors' and p2 == 'paper') or \
         (p1 == 'paper' and p2 == 'rock'):
        print("Player 1 wins!")
        wins += 1
    else:
        print("Player 2 wins!")
        losses += 1

print(f'Wins: {wins}, Losses: {losses}')

#wins: 1, losses: 1

# - Allow choosing how many human players there are, from 0-2?

choices = ['rock', 'paper', 'scissors']

num_players = int(input("How many human players? (0-2) "))

if num_players < 0 or num_players > 2:
    print("Invalid number of players. Please choose a number between 0 and 2.")
else:
    wins = 0
    losses = 0

    num_rounds = int(input("How many rounds do you want to play? "))

    for _ in range(num_rounds):
        p1 = ""
        p2 = ""

        if num_players >= 1:
            p1 = input('Player 1, pick one of rock, paper, or scissors (or type "quit" to end): ').lower()

            if p1 == 'quit':
                break

            if p1 not in choices:
                print('Invalid choice. Please pick either rock, paper, or scissors.')
                continue

        if num_players == 2:
            p2 = input('Player 2, pick one of rock, paper, or scissors (or type "quit" to end): ').lower()

            if p2 == 'quit':
                break

            if p2 not in choices:
                print('Invalid choice. Please pick either rock, paper, or scissors.')
                continue

        if num_players == 0:
            p1 = random.choice(choices)
            p2 = random.choice(choices)
        elif num_players == 1:
            p2 = random.choice(choices)

        print(f'Player 1 chose: {p1}')
        print(f'Player 2 chose: {p2}')

        if p1 == p2:
            print("It's a tie!")
        elif (p1 == 'rock' and p2 == 'scissors') or \
             (p1 == 'scissors' and p2 == 'paper') or \
             (p1 == 'paper' and p2 == 'rock'):
            print("Player 1 wins!")
            wins += 1
        else:
            print("Player 2 wins!")
            losses += 1

    print(f'Wins: {wins}, Losses: {losses}')

# - Organize everything into functions?

def get_player_choice(player_num):
    while True:
        choice = input(f'Player {player_num}, pick one of rock, paper, or scissors (or type "quit" to end): ').lower()
        if choice == 'quit':
            return None
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print('Invalid choice. Please pick either rock, paper, or scissors.')

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return "It's a tie!"
    elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
         (p1_choice == 'scissors' and p2_choice == 'paper') or \
         (p1_choice == 'paper' and p2_choice == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game(num_players, num_rounds):
    wins = 0
    losses = 0

    for _ in range(num_rounds):
        p1 = get_player_choice(1) if num_players >= 1 else get_computer_choice()
        if p1 is None:
            break

        p2 = get_player_choice(2) if num_players == 2 else get_computer_choice()
        if p2 is None:
            break

        print(f'Player 1 chose: {p1}')
        print(f'Player 2 chose: {p2}')

        result = determine_winner(p1, p2)
        print(result)

        if result == "Player 1 wins!":
            wins += 1
        elif result == "Player 2 wins!":
            losses += 1

    print(f'Wins: {wins}, Losses: {losses}')

def main():
    num_players = int(input("How many human players? (0-2) "))
    if num_players < 0 or num_players > 2:
        print("Invalid number of players. Please choose a number between 0 and 2.")
        return

    num_rounds = int(input("How many rounds do you want to play? "))
    play_game(num_players, num_rounds)

if __name__ == "__main__":
    main()

# - Organize everything into classes??

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.wins = 0
        self.losses = 0

    def get_player_choice(self, player_num):
        while True:
            choice = input(f'Player {player_num}, pick one of rock, paper, or scissors (or type "quit" to end): ').lower()
            if choice == 'quit':
                return None
            if choice in self.choices:
                return choice
            print('Invalid choice. Please pick either rock, paper, or scissors.')

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, p1_choice, p2_choice):
        if p1_choice == p2_choice:
            return "It's a tie!"
        elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
             (p1_choice == 'scissors' and p2_choice == 'paper') or \
             (p1_choice == 'paper' and p2_choice == 'rock'):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

    def play_game(self, num_players, num_rounds):
        for _ in range(num_rounds):
            p1 = self.get_player_choice(1) if num_players >= 1 else self.get_computer_choice()
            if p1 is None:
                break

            p2 = self.get_player_choice(2) if num_players == 2 else self.get_computer_choice()
            if p2 is None:
                break

            print(f'Player 1 chose: {p1}')
            print(f'Player 2 chose: {p2}')

            result = self.determine_winner(p1, p2)
            print(result)

            if result == "Player 1 wins!":
                self.wins += 1
            elif result == "Player 2 wins!":
                self.losses += 1

        print(f'Wins: {self.wins}, Losses: {self.losses}')

def main():
    num_players = int(input("How many human players? (0-2) "))
    if num_players < 0 or num_players > 2:
        print("Invalid number of players. Please choose a number between 0 and 2.")
        return

    num_rounds = int(input("How many rounds do you want to play? "))

    game = RockPaperScissors()
    game.play_game(num_players, num_rounds)

if __name__ == "__main__":
    main()



from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)
