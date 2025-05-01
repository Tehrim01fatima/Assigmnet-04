SENTENCE_IN_START:str ="Code in Place is fun. I learned to program and used Python to make "

def main():

    adjective:str= str(input("please type an adjective and press enter."))
    noun:str=str(input("Please type a  noun and press enter."))
    verb:str= str(input("please type a verb and press enter"))


    print(SENTENCE_IN_START + adjective + " " + noun + " " + verb + "!")


if __name__ == '__main__':
    main()           