import random

DONE_LIKELIHOOD = 0.2  

def done():
    """Returns True with probability DONE_LIKELIHOOD to signal early stopping."""
    if random.random() < DONE_LIKELIHOOD:
        print("  (Stopping early because I feel like it!)")  # Optional feedback
        return True
    return False

def chaotic_counting():
    """Counts from 1 to 10, but may stop early based on randomness."""
    for i in range(10):
        curr_num = i + 1
        if done():
            return  
        print(curr_num)

def main():
    """Main program execution."""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.\n")
    chaotic_counting()
    print("\nI'm done!")

if __name__ == "__main__":
    main()