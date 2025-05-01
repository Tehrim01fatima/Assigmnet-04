INCHES_IN_FOOT=12

def main():
    
   feet= float(input("\033[1;3m Enter number of feet:"))
   inches:float= feet*INCHES_IN_FOOT
   print(f"There is {inches} inches in {feet} feet")

if __name__ == '__main__':
    main()