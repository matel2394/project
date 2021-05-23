#문제 5

def solution(arr):
    left,right = 0,len(arr)-1
    #왼쪽 -0  오른쪽=0 숫자갯수
    while left<right: #오른쪽이 더 클때에만
        arr[left],arr[right] = arr[right],arr[left]
        #첫번째값[왼],첫번째값[오른쪽] = 첫번째값[오른쪽],첫번째값[왼쪽]
        left += 1 #왼쪽 1증가
        right -= 1 #오른쪽 1 감소
    return arr

    #left 0일경우 right 0=> 반복문 실행
        #arr[0],arr[0] = arr[0],arr[0]
          #1     #1        #1    #1
        #left +1 right -1
    #left 1일경우 right -1
        #arr[1],arr[-1] = arr[-1],arr[1]
         #4     #3          #3      #4
        #left +1  right -1
    #left 2일경우 right -2
       #arr[2] , arr[-2].

arr = [1,4,2,3]
ret =solution(arr)

print("solution: return value of the function is",ret,".")
