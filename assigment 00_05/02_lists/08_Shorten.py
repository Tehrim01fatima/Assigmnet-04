MAX_LENGTH:int= 3


def shorten(lst):
    while len(lst)>MAX_LENGTH:
        last_element=lst.pop
        print(last_element)

def get_list():
    lst=[]
    val=input("Please enter an element of the list or press enter to stop.")
    while val != "":
        lst.append(val)
        val= input(" Please enter an element of the list or press enter to stop.")
    return lst
def main():
    lst = get_list()
    shorten(lst)



if __name__ == '__main__':
    main()