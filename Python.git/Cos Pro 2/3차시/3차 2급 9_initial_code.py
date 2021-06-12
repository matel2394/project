def solution(day, numbers): #day 변수와 numbers를 파라미터로 사용하는 함수
    count = 0 #count 함수에 0 대입
    for number in numbers: #number에 numbers 내용물 넣으면서 6회 반복
        if number%2 == day%2: #만약 number을 2로 나눈것의 나머지가 day를 2로 나눈것의 나머지와 같다면
            count += 1 #count 변수에 1 추가
    return count #count 리턴

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")