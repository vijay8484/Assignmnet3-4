def main():
    print("In Main")
    num1 = int(input("Enter the No of Element 1 :"))
    num2 = int(input("Enter the No of Element 2 :"))

    result = multiply(num1, num2)
    print(result)


multiply = lambda no1, no2: no1 * no2

if __name__ == '__main__':
    main()
