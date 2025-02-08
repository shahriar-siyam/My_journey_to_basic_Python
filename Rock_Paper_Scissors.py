# print("Let's play rock_paper_scissors")
# player1=input("Player1:")
# player2=input("Player2:")
# if player1=="rock" and player2=="paper":
#     print("player2 wins")
# elif player1=="rock" and player2=="scissors":
#     print("player1 wins")
# elif player1=="paper" and player2=="scissors":
#     print("player2 wins")
# elif player1=="paper" and player2=="rock":
#     print("player1 wins")
# elif player1=="scissors" and player2=="rock":
#     print("player2 wins")
# elif player1=="scissors" and player2=="paper":
#     print("player2 wins")
import random
def rps():
    print("Welcome to ROCK PAPER SCISSOR")
    player=input("Player:")
    computer=random.choice(["r","p","s"])
    print("Player:",player)
    print("Computer:",computer)

    if player==computer:
        print("Game is drawn")
    elif player=="r" and computer=="s":
        print("player wins")
    elif player=="r" and computer=="p":
        print("computer wins")
    elif player == "p" and computer == "s" :
        print("computer wins")
    elif player == "p" and computer == "r":
        print("player wins")
    elif player == "s" and computer == "p":
        print("player wins")
    elif player == "s" and computer == "r":
        print("computer wins")


rps()