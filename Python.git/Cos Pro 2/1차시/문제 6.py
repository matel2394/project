def solution(number):
    count = 0 #박수 횟수
    for i in range(1,number + 1): #1부터 40까지 반복
        current = i
        temp = count #임시변수에 박수횟수 저장
        while current != 0: #0이 아닐때까지 반복
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9 : #
                count += 1 #박수 횟수 올리기
                print("pair",end = ' ')
            current = current // 10 #현재 숫자 // 10 자릿수 내리기
        if temp == count:
            print(i,end=' ')
    print(" ",end= ' ')
    return count

number =40
ret = solution(number)
print("solution: return value of the function is",ret,".")
