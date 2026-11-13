import random
print("Welcome to 🪨  Rock-📄  Paper-✂️  Scissors!")
print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock\n")
print("1: Rock | 2: Paper | 3: Scissors")
def check():
    while True:
        user = int(input("Enter your choose: "))
        if user < 1 or user > 3:
            print("Invalid move run again and choose between 1 to 3")
            break;
        else:
            if user == 1:
                print(f"User choose 🪨  Rock now 🖥️  computers turns");
            elif user == 2:
                print("User choose 📄  Paper now 🖥️  computers turns");
            elif user == 3:
                print("User choose ✂️  Scissors now 🖥️  computers turns");
        computer = random.randint(1,3)
        if computer == 1:
            print("🖥️  computer choose: 🪨  Rock")
        elif computer == 2:
            print("🖥️  computer choose: 📄  Paper")
        elif computer == 3:
            print("computer choose: ✂️  Scissors")
        if (computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2):
            print("🖥️   Computer win")
            break
        elif (computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1):
            print("user win")
            break;
        else:
            print("Drawn match")
            break;
check()
while True:
    ask_user = input("Do you play anagin? then enter y/n: ").lower()
    if ask_user == "y":
        check();
    else:
        print("Thanks for playing the game!")
        break
