is_running = True

while is_running:

    import random
    print("Let\'s play Rock, Paper, Scissors!")
    R = "rock"
    P = "paper"
    S = "scissor"

    choice_list = [R, P, S]

    user_input = input(
        "What option would you like to pick?\n['R', 'P', 'S'] : ")
    if user_input == "R":
        cpu_choice = random.choice(choice_list)
        print("Player(", R, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == R:
            print("Tie")
            continue

        elif cpu_choice == P:
            print("Computer Wins")
            
        elif cpu_choice == S:
            print("You Win")

    elif user_input == "S":
        cpu_choice = random.choice(choice_list)
        print("Player(", S, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == S:
            print("Tie")
            continue

        elif cpu_choice == P:
            print("You Win")

        elif cpu_choice == R:
            print("Computer Wins")

    elif user_input == "P":
        cpu_choice = random.choice(choice_list)
        print("Player(", P, ")", ":", "CPU(", cpu_choice, ")")

        if cpu_choice == P:
            print("Tie")
            continue


        elif cpu_choice == S:
            print("Computer Wins")

        elif cpu_choice == R:
            print("You Win")

    else:
        print("Invalid Entry. Try again")
        continue

    continue_choice = input("Would you like to play again? [y,n] :")
    if continue_choice == "y":
        pass
    if continue_choice == "n":
        is_running = False

        print("The Rock births the Scissor and the Scissor is the death of the Paper.")