import random


def repeat() :
    user_action = input("Enter Your Choice (Stone,Paper,Scissor) :  ")
    possible_action = ["Stone", "Paper", "Scissor"]
    computer_action = random.choice(possible_action)

    if computer_action == user_action:
        print("Its a Tie.")

    elif user_action == "Stone":
        if computer_action == "Paper":
            print("Computer Choice : ", computer_action)
            print("Computer Wins!")

        else:
            print("Computer Choice : ", computer_action)
            print("You Win!")

    elif user_action == "Paper":
        if computer_action == "Scissor":
            print("Computer Choice : ", computer_action)
            print("Computer Wins!")
        else:
            print("Computer Choice : ", computer_action)
            print("You Win!")

    elif user_action == "Scissor":
        if computer_action == "Stone":
            print("Computer Choice : ", computer_action)
            print("Computer Wins!")
        else:
            print("Computer Choice : ", computer_action)
            print("You Win!")


repeat()
while True:
    play_again = input("Do you want to play again ? ")

    if play_again == "yes" :
        repeat()
    else:
        print("Thank you!")
        break




