import sys

max = -sys.maxsize - 1
min = sys.maxsize

num = [8, 7, 3, 2, 9, 4, 1, 6, 5]

for i in range(len(num)): #num값이 아무리 바뀌어도 정수라서이다.
    if min >= num[i]:
        min = num[i] #min값을 최대로 놔두고 하나씩 비교하면서 값을 줄이기
    if max <= num[i]:
        max = num[i] #max값을 최소로 놔두고 하나씩 비교하면서 값을 늘리기
print("최댓값 :", max)
print("최솟값 :", min)
     
