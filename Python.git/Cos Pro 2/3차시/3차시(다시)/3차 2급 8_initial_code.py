def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]): #2~8 #1~6 3~5
            used_tv[i] = used_tv[i] + 1 #1번째 인덱스에 2번째 인덱스의 요소에 1을 더해서 앞쪽 인덱스로 대입
            # [0,1,1,1,1,1,0,0,0,0,0,0,...]
            # [0,1,2,2,2,2,1,1,0,0,0,0,...]
            # [0,1,2,3,3,2,1,1,0,0,0,0,...]
    for i in used_tv:
        if i >= 2:
            answer = answer + 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

used_tv = [0] * 25
for program in programs:
    for i in range(program[0], program[1]):
        used_tv[i] = used_tv[i]+1
print(used_tv)