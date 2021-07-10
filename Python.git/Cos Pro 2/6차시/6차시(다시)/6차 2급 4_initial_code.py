#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    #여기에 코드를 작성해주세요.
    answer = 0
    list = [0,0,0]
    for i in cards:
        if i[0] == "blue":
            list[0] += 1
        if i[0] == "red":
            list[1] += 1
        if i[0] == "black":
            list[2] += 1
        answer += int(i[1])
    if 3 in list:
        answer = answer*3
    elif 2 in list:
        answer = answer*2
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")