def main():
    dividend= int(input("Please Enter an integer to be divided:"))
    divisor= int(input("Enter the integer to divided by:"))

    quotient:int= dividend// divisor
    remainder:int= dividend % divisor

    print(f"The result of this division is: {quotient} with the remaidner of {remainder}")


if __name__ == '__main__':
    main()