import random

mylist = ['Rock', 'Paper', 'Scissors']

computer = random.choice(mylist)

user = input("Pick an option between 'Rock','Paper'and'Scissors':  ")

print("computer: ", computer)
print("user: ", user)
if computer == user:
    print("That's a tie")
elif user not in mylist:
    print("Error. Try again later")
elif computer != user:
    print("You're the winner")
