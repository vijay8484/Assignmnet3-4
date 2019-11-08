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

    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    print("Largest number in given List is :", max)


if __name__ == '__main__':
    main()
