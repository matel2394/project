def solution(programs): #programs를 파라미터로 사용하는 sloution함수 디파일
    answer = 0 #answer 함수에 0 대입
    used_tv = [0] * 25 #used tv 리스트의 0번째 인덱스에 25 곱하기

    for program in programs: #program에 programs 내용물 넣으면서 반복
        for i in range(program[0], program[1]): #i에 program의 0번째와 1번째 인덱스를 넣으며 반복
            used_tv[i] = used_tv[i] + 1 #used tv의 i 인덱스에 used tv의 i 인덱스에서 1을 추가한걸 대입
    
    for i in used_tv: #used tv의 내용을 i에 넣으며 반복
        if i >= 2: #만약 i가 2보다 크거나 같으면
            answer = answer + 1 #answer 변수에 answer +1 만큼 추가함
    return answer #answer 변수 리턴

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전 : solution 함수의 반환 값은 7 입니다.

#수정 후 :solution 함수의 반환 값은 4 입니다.

#문제에서 원하는 내용 : A씨가 Tv를 2대 틀어놓는 시간 구하기