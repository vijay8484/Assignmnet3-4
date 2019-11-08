def main():
    print("In Main")
    num = int(input("Enter the No of Element :"))
    result = checkPow(num)
    print(result)


checkPow = lambda no: pow(no, 2)

if __name__ == '__main__':
    main()
