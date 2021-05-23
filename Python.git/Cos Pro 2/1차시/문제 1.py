# 문제1 : 리스트에 저장된 문자열의 갯수를 다시 리스트에 담기
def soluthon(shirt_size):  # 함수만들기
    # 지문보고 문제풀기 ~~~~~
    size_count = [0, 0, 0, 0, 0, 0] #1. 티셔츠 사이즈별 개수를 담음 리스트 선언
                #xs #s #m #L #xL #XXl
    for ss in shirt_size:  # 리스트 반복 => 리스트내 항목이 변수에 하나씩 대입
        if ss == "XS": #만약에 XS이면 첫번째 인덱스 +1
            size_count[0] += 1
        if ss == "S":  #만약에 S이면 두번째인덱스 +1
            size_count[1] += 1
        if ss == "M":  #만약에 S이면 세번째인덱스 +1
            size_count[2] += 1
        if ss == "L":  #만약에 S이면 네번째인덱스 +1
            size_count[3] += 1
        if ss == "XL": #만약에 S이면 다섯번째인덱스 +1
            size_count[4] += 1
        if ss == "XXL":#만약에 S이면 여섯번째인덱스 +1
            size_count[5] += 1
    return size_count

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = soluthon(shirt_size)  # 함수 불러내기

print("solution: return value of the function is", ret, " .")

