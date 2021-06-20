def solution(korean, english): #필요 수학점수 구하기 함수
    answer = 0 #수학점수 변수
    math = 210 - (korean + english) #국어와 영어를 먼저 더해서 210에서 뺀 값이 수학점수가 된다
    if math > 100: #만약 수학점수가 100점을 넘어야 평균 70이 된다면
        answer = -1 #만점이 100점이라 평균 70점은 불가능하기때문에 수학점수는 -1로 표기한다
    else: #100을 넘지않는다면
        answer = math #answer은 수학점수다
    return answer #리턴

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
korean = 70
english = 60
ret = solution(korean, english)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전: solution 함수의 반환 값은 -1 입니다.

#수정 후:solution 함수의 반환 값은 80 입니다.

#문제에서 원하는 내용:평균점수가 70점이 나오기 위해 필요한 수학의 점수