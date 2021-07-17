def solution(number):
    answer = 0
    for i in range(1,number+1):
        current = i
        temp = answer
        while current != 0:
            if current%10 == 3 or current%10 == 6 or current%10 == 9:
                answer+= 1
                print("pair",end='')
            current = current//10
        if temp == answer:
            print(i,end = '')
        print(" ",end='')
    print("")
    return answer


number = 40
print(solution(number))