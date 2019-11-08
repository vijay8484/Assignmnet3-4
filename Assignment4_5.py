from functools import reduce


def AcceptData():
    arr = list()
    size = int(input("Enter the no of element"))
    for i in range(0, size, 1):
        print("Enter the no", i + 1)
        no = int(input())
        arr.append(no)

    return arr


def PrimeNo(no):
    if no > 1:
        for i in range(2, no, 1):
            if (no % i) == 0:
                break
            else:
                return no


def Max(no1, no2):
    if no1 > no2:
        return no1


def main():
    rawData = AcceptData()
    print("Raw Data is here")
    print(rawData)

    filteredData = list(filter(PrimeNo, rawData))
    print("Filtered Data is Here :")
    print(filteredData)

    ModifiedData = list(map(lambda no: no * 2, filteredData))
    print("Modified Data is")
    print(ModifiedData)

    if len(ModifiedData) > 0:
        result = reduce(lambda no1, no2: no1 if no1 > no2 else no2, ModifiedData)
        print("Final result is", result)
    else:
        print("No result")


if __name__ == "__main__":
    main()
