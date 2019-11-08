def main():
    print("In Main")
    fun()


def fun():
    print("In fun")
    arr = list()
    count = 0
    num = input("Enter the No of Element :")
    for i in range(0, int(num), 1):
        no = input("Num :")

        arr.append(int(no))

    print(arr)
    searchNo = int(input("Enter the element to search :"))

    for i in range(0, len(arr)):
        if searchNo == arr[i]:
            count = count + 1

    print(count)


if __name__ == '__main__':
    main()
