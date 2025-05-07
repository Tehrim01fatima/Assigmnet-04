import random 

ROUND_NUM = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for i in range(ROUND_NUM):
        print("Round", i + 1)  # Fixed: Changed "i + i" to "i + 1"

        # Generate random numbers
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)  # Fixed: Corrected typo "radint" to "randint"
        print("Your number is", your_num)
        
        # Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()  # Added .lower()

        # Map out all the ways to win the round
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num
        
        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            your_score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_num)
        
        # Keep track of your score
        print("Your score is now", your_score)  # Fixed typo "Ypur" to "Your"
        print()

    print("Thanks for playing")

if __name__ == "__main__":
    main()