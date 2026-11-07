import random
#Set True to use the fixed choices given in the test cases.
#Set False to play with random computer choices.
TEST_MODE = True
def find_winner(player, computer):
    if player == computer:
        return "draw"
    elif(player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"): return "player"
    else:
        return "computer"
    
def play_game():
    choices = ["rock", "paper", "scissors"] 
    fixed_choices = ["scissors", "rock", "paper"]
    player_score = 0
    computer_score = 0
    draw_score = 0

    print("\n===== ROCK PAPER SCISSORS =====")

    for round_num in range(3):

        # Take valid player input
        while True:
            player = input(
                f"Round {round_num + 1} - Enter rock, paper or scissors: "
            ).lower().strip()

            if player in choices:
                break
            else:
                print("Invalid choice. Enter rock, paper or scissors.")

        # Computer choice
        if TEST_MODE:
            computer = fixed_choices[round_num]
        else:
            computer = random.choice(choices)

        print("Computer chose:", computer)

        # Find round winner
        result = find_winner(player, computer)

        if result == "player":
            print(f"Round {round_num + 1}: You win")
            player_score += 1

        elif result == "computer":
            print(f"Round {round_num + 1}: Computer wins")
            computer_score += 1

        else:
            print(f"Round {round_num + 1}: Draw")
            draw_score += 1

    # Display final score
    print("\n===== FINAL SCORE =====")
    print("You:", player_score)
    print("Computer:", computer_score)
    print("Draws:", draw_score)

    # Declare match result
    if player_score > computer_score:
        print("Result: You win the match!")
    elif computer_score > player_score:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")

    print("Thanks for playing!")
#Play again option
while True: 
    play_game()
    again = input("\nPlay again? (yes/no): ").lower().strip()

    if again != "y":
        print("Thank you for playing!")
        break