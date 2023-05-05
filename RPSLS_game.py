import random
import time

# Constant income box
win_move = {
    "rock": ["lizard", "scissors"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}
count = 0
PlayerWin = 0
SheldonWin = 0
fool = "Not the sharpest tool in the shed I see. You needed to type an integer."

# game body
print("What is your name?")
name = input(" ")
print(f"Knock-Knock-Knock, {name}!")
print(f"Knock-Knock-Knock, {name}!")
print(f"Knock-Knock-Knock, {name}!")
print(
    f"I'm coming in. Greetings, {name}, my name is Sheldon. I heard that you're good at "
                                          "Rock-Paper-Scissors-Lizard-Spock. I suggest we play and find out")
game = input("Do you agree? (yes - Enter, no - space bar)")
if game == " ":
    print("You're passing? No surprise, you don't look smart enough. Bazinga!")
    exit()
else:
    print("How many rounds wold you like to take?")
rounds = input(" ")
try:
    tmp = int(rounds)
except ValueError as e:
    print(
        f"{fool}. I don't think we can play when you make mistakes so early in the game, so... better luck nex ' \
                           'time."
               "And a piece of advice, from me to you, grow some gray matter, will you?")

if int(rounds) > 20:
    print("Ambitious, I like your scale. Hope you understand that you can not quit midway...")

print("So let's begin then")
while count < int(rounds):
    while True:
        index = int(input("Make your choice: 0-rock, 1-paper, 2-scissors, 3-lizard, 4-spock "))
        if index in range(len(list(win_move.keys()))):
            break  # exit cycle
        print(f"{fool}. And in range of listed above. Try again")
    player_move = list(win_move.keys())[index]
    computer_move = random.choice(list(win_move.keys()))
    print(f"{name}'s move: {player_move}")
    print(f"Sheldon's move: {computer_move}")
    if computer_move in win_move[player_move]:
        print("Sheldon: Oh, you won. According to the string theory that was just a coincidence")
        PlayerWin += 1
    elif player_move == computer_move:
        print("Sheldon: It's a tie. I don't acknowledge ties")
    else:
        print("Sheldon: I won. Expected as much")
        SheldonWin += 1
    count += 1

print(f"Oh well, that's unfortunate. We've played only {str(count)} rounds")
if PlayerWin > SheldonWin:
    print(f"Yours {str(PlayerWin)} out of {str(rounds)}. OK you won. It was nearly impossible but fine")
elif PlayerWin == SheldonWin:
    print(f"Yours {str(PlayerWin)} out of {str(rounds)}. We're even. It'll be wise to play again")
else:
    print(f"Yours {str(PlayerWin)} out of {str(rounds)}. Vini, vidi, vici. I won")
time.sleep(5)
