print("Let's play rock_paper_scissors")
player1=input("Player1:")
player2=input("Player2:")
if player1=="rock" and player2=="paper":
    print("player2 wins")
elif player1=="rock" and player2=="scissors":
    print("player1 wins")
elif player1=="paper" and player2=="scissors":
    print("player2 wins")
elif player1=="paper" and player2=="rock":
    print("player1 wins")
elif player1=="scissors" and player2=="rock":
    print("player2 wins")
elif player1=="scissors" and player2=="paper":
    print("player2 wins")
