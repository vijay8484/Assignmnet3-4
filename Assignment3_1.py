def main():
    print("In Main")
    fun()


def fun():
    print("In fun")
    arr = list()
    sum = 0
    num = input("Enter the No of Element :")
    for i in range(0, int(num), 1):
        no = input("Num :")

        arr.append(int(no))

    for i in arr:
        sum = sum + i

    print(sum)


if __name__ == '__main__':
    main()
