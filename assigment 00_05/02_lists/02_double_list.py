def main():
    numbers:list[int]=[1,2,3,4,]
    for i in range(len(numbers)):
        elements=numbers[i]
        numbers[i]=elements*2
        print(numbers)

if __name__ == '__main__':
    main()