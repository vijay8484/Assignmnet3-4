def main():
    print("In Main")
    fun()


def fun():
    print("In fun")
    arr = list()
    num = input("Enter the No of Element :")
    for i in range(0, int(num), 1):
        no = input("Num :")

        arr.append(int(no))

    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]

    print("Minimum number in given List is :", min)


if __name__ == '__main__':
    main()
