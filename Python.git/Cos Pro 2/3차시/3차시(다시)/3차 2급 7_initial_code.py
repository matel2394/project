def solution(num_apple, num_carrot, k):
    answer = 0 #주스 수
    
    if num_apple < num_carrot * 3: #사과 수가 당근*3 한것보다 작으면
        answer = num_apple // 3 #사과를 3으로 나누고 몫만 챙긴 뒤 앤서에 대입
    else: #아니면
        answer = num_carrot    #앤서에 당근 수를 대입

    num_apple -= answer * 3 #2  # 1
    num_carrot -= answer #0  #-4

    i = 0
    while k - (num_apple + num_carrot + i) > 0: #4 에 -3에 i더해서 뺀 값이 0보다 크면 계속 반복
        if i % 4 == 0: #만약 0을 4로 나눈것의 나머지가 0이라면
            answer += 1 #카운트에 1 추가
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