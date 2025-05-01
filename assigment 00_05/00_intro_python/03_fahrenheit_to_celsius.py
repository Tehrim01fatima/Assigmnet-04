def main():
    
   fahrenheit= float(input("\033[1;3m Enter temperature in fahrenheit:"))
   celsius= (fahrenheit -32)*5.0/9.0
   print (f"temperature :{fahrenheit}F = {celsius}C")


if __name__ == '__main__':
    main()