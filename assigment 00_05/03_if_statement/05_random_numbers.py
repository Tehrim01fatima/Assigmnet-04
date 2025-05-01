import random

NUM= 6
MIN_NUM= 1
MAX_NUM= 6


def main():
     for i in range(NUM):
          number= random.randint(MIN_NUM,MAX_NUM)
          print(number, end='')

print()


if __name__ == '__main__':
    main()