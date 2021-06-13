def solution(tile_length): #tile_length를 파라미터로 하는 solution함수 디파일 (타일 색칠 순서 구하기 함수)
    answer = '' #answer 변수에 ''대입
    com = 'RRRGGB' #com 변수에 RRRGGB 대입
    if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6 == 4: #만약 tile_length를 6으로 나눴을때 나머지가 1이나 2나 4라면
        answer = '-1' #answer 변수에 문자열 -1 대입
    else: #아니면
        for i in range(tile_length): #tile_length의 항목을 i에 대입하며 반복
            answer += com[i % 6] # #answer 변수에 i를 6으로 나눈것의 나머지번의 com의 인덱스를 더함
    return answer #answer 변수를 리턴함

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
tile_length1 = 11
ret1 = solution(tile_length1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

tile_length2 = 16
ret2 = solution(tile_length2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")

# 수정 전: ???

#수정 후 : solution 함수의 반환 값은  RRRGGBRRRGG  입니다.
#solution 함수의 반환 값은  -1  입니다.

#문제에서 원하는 내용:타일을 색칠한 순서를 구하기 (안되면 -1로)
