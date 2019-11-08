from functools import reduce


def AcceptData():
    arr = list()
    size = int(input("Enter Number of element"))

    for i in range(0, size, 1):
        print("Enter the no :", i + 1)
        no = int(input())
        arr.append(no)

    return arr


def main():
    rawData = AcceptData()
    print("Accepted data is here")
    print(rawData)

    FilteredData = list(filter(lambda no:  (70 <= no <= 90), rawData))
    print("Filtered Data is")
    print(FilteredData)

    ModifiedData = list(map(lambda no: no + 10, FilteredData))
    print("Modified Data is")
    print(ModifiedData)

    if len(ModifiedData) > 0:
        result = reduce(lambda no1, no2: no1 * no2, ModifiedData)
        print("Final result is", result)
    else:
        print("No result")


if __name__ == "__main__":
    main()
