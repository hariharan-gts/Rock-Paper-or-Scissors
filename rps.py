import random


def game():
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    player=None

    while player not in choices:
        player=input("rock,paper or scissors?:").lower()

    if(player==computer):
        print("player:",player)
        print("computer:",computer)
        print("Tie!")
    elif player=="rock":
        if computer=="scissors":
          print("player:",player)
          print("computer:",computer)
          print("You win!")
        if computer=="paper":
          print("player:",player)
          print("computer:",computer)
          print("You Lose!")
    elif player=="paper":
        if computer=="scissors":
          print("player:",player)
          print("computer:",computer)
          print("You Lose!")
        if computer=="rock":
          print("player:",player)
          print("computer:",computer)
          print("You win!")
    elif player=="scissors":
       if computer=="paper":
          print("player:",player)
          print("computer:",computer)
          print("You Lose!")
       if computer=="rock":
          print("player:",player)
          print("computer:",computer)
          print("You Lose!")




def main():
    game()
    chc=input("You want to play again[Y/N]?:").upper()
    while chc=="Y":
        game()
        chc=input("You want play again[Y/N]?:").upper()
        

if __name__=="__main__":
    main()
    