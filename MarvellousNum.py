def ChkPrime(list1):
    temp = list()
    for no in list1:
        if no > 1:
            # check for factors
            for i in range(2, no):
                if (no % i) == 0:
                    break
            else:
                print(no, "is a prime number")
                temp = temp.append(no)

    return temp
