def OddEven(num):
    numStr = str(num)
    sum = 0
    for i in range(0, len(numStr)):
        sum += int(numStr[i])
        i += 1
    if sum % 2 == 0:
        print("Even")
    else:
        print("Oddish")


OddEven(200)
