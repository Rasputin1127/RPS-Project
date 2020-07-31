import random
comp_wins = 0
player_wins = 0
winning_score = 3
while comp_wins < winning_score and player_wins < winning_score:
    print("Ro...Sham...BO!")
    print(f"Player Score: {player_wins} Computer Score: {comp_wins}")
    p1 = input("What do you throw?").lower()
    if p1 == "quit" or p1 == "q":
        break
    p2 = random.randint(0, 2)
    if p2 == 0:
        p2 = "rock"
        print("Your opponent threw rock!")
    elif p2 == 1:
        p2 = "scissors"
        print("Your opponent threw scissors!")
    else:
        p2 = "paper"
        print("Your opponent threw paper!")
    if p1 == p2:
        print("It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            print("You win!")
            player_wins += 1
        else:
            print("You lose! Who throws rock?")
            comp_wins += 1
    elif p1 == "scissors":
        if p2 == "rock":
            print("You lose! Who throws scissors?")
            comp_wins += 1
        else:
            print("You win!")
            player_wins += 1
    elif p1 == "paper":
        if p2 == "rock":
            print("You win!")
            player_wins += 1
        else:
            print("You lose! Who throws paper?")
            comp_wins += 1
    else:
        print("You cheated!")
print(f"Player Score: {player_wins} Computer Score: {comp_wins}")
if comp_wins == winning_score:
    print("The Computer wins!")
elif comp_wins == player_wins:
    print("It's a Tie!")
else:
    print("You win! Congratulations!")
