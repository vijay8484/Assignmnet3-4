from MarvellousNum import *


def main():
    print("In Main")
    ListPrime()


def ListPrime():
    print("In ListPrime")
    arr = list()
    count = 0
    num = input("Enter the No of Element :")
    for i in range(0, int(num), 1):
        no = input("Num :")

        arr.append(int(no))

    primelist = ChkPrime(arr)

    for i in primelist:
        count = count + i

    print(count)


if __name__ == '__main__':
    main()
