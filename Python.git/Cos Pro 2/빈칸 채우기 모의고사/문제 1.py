def solution(arr):
   left,right = 0, len(arr) - 1
   while left<right:
       arr[left],arr[right] = arr[right],arr[left]
       #1,2 = 2,1
       left +=1
       right-=1
   return arr




arr = [1,4,2,3]
print(solution(arr))