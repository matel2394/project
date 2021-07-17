def solution(tile):
    answer = ""
    com = 'RRRGGB'
    if tile%6 ==1 or tile%6 ==2 or tile%6 == 4:
        answer = '-1'
    else:
        for i in range(tile):
            answer += com[i%6]
    return answer


tile1 = 11
print(solution(tile1))
tile2 = 16
print(solution(tile2))