def solution(num_apple, num_carrot, k):
    answer = 0 #주스 수
    
    if num_apple < num_carrot * 3: #10 < 15
        answer = num_apple // 3 # answer =3
    else: #아니면
        answer = num_carrot # X   #answer = 1

    num_apple -= answer * 3 # 10 - 9 = 1      #2
    num_carrot -= answer # 5 - 3 = 2        #0

    i = 0 #뭔갈 더 빼야하는 갯수를 알려주는 카운터?
    while k - (num_apple + num_carrot + i) > 0: #4- (3 + i) >0 #여기서 i가 1이 되어야 while문이 종료됨
        if i % 4 == 0: #0을 4로 나누면 0이 되니까 k - (J+i) = 0을 충족하지 못함
            answer -= 1 #재료가 하나 빠지니 주스 하나를 더 만들수 없어 1이 빠짐
            #answer += 1
        i = i + 1 #i = 1 , i=3, i = 5
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")