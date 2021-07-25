def solution(number):
    count = 0
    for i in range(1, number + 1): #1부터 40
        current = i #1,2,3,4,5...
        temp = count #0
        while current != 0: #current가 0이 아닐때까지 반복
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

#The following is code to output testcase.
number = 40
ret = solution(number)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")