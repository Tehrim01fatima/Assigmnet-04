import math
def main():
    ab:float= float(input("\033[1;3m Enter the length of AB:"))
    ac:float= float(input("\033[1;3m Enter the length of AC:"))

    bc:float= math.sqrt(ab**2+ ac**2)
    print(f"the length of BC (the hypotenuse) is :{bc}")

    
if __name__ == '__main__':
    main()