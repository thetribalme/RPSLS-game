import random

# Constant income box
computer_list = ["rock", "paper", "scissors", "lizard", "spock"]
win_move = {
    "rock": ["lizard", "scissors"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}
player_list = ["rock", "paper", "scissors", "lizard", "spock"]

computer = random.choice(computer_list)
count = 0
PlayerWin = 0
SheldonWin = 0
fool = "Not the sharpest tool in the shed I see. You needed to type an integer."

# game body
print("What is your name? ")
name = input(" ")
print("Knock-Knock-Knock, " + name + "!")
print("Knock-Knock-Knock, " + name + "!")
print("Knock-Knock-Knock, " + name + "!")
print(
    "I'm coming in. Greetings, " + name + ", my name is Sheldon. I heard that you're good at "
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

    if int(rounds) > 20:
        print("Ambitious, I like your scale. Hope you understand that you can not quit midway...")

    print("So let's begin then")
    while count < int(rounds):
        index = int(input("Make your choice: 0-rock, 1-paper, 2-scissors, 3-lizard, 4-spock "))
        try:
            temp = index in range(5)
            player = player_list[index]
            print(name + "'s move: " + player)
            print("Sheldon's move: " + computer)
            if win_move[player] == computer:
                print("Sheldon: Oh, you won. According to the string theory that was just a coincidence")
                PlayerWin = PlayerWin + 1
            elif player == computer:
                print("Sheldon: It's a tie. I don't acknowledge ties")
            else:
                print("Sheldon: I won. Expected as much")
                SheldonWin = SheldonWin + 1
            count = count + 1
        except:
            print(fool + " Ant in range of listed above. Try again")

    print("Oh well, that's unfortunate. We played only " + str(count) + " rounds")
    if PlayerWin > SheldonWin:
        print("Yours " + str(PlayerWin) + " out of " + str(rounds) + ". OK you won. It was nearly impossible but fine")
    elif PlayerWin == SheldonWin:
        print("Yours " + str(PlayerWin) + " out of " + str(rounds) + ". We're even. It'll be wise to play again")
    else:
        print("Yours " + str(PlayerWin) + " out of " + str(rounds) + ". Vini, vidi, vici. I won")
    exit()
except:
    if count == 0:
        print(
            fool + "I don't think we can play when you make mistakes so early in the game, so... better luck nex time."
                   "And a piece of advice, from me to you, grow some gray matter, will you?")
    else:
        exit()
