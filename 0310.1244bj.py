### 내가 짠 코드 ###
# 인덱스를 보정해야 되고, 여학생 대칭 코드 작성 부분이 틀림
# 델타와 비슷하게 좌우로 찾아가면서 해결하려고 했는데, 잘 되지 않음

'''
N = int(input())

arr = list(map(int, input().split()))

nums_student = int(input())

gender, nums = map(int, input().split()) 

dj = [-1, 1]

for i in range(1, len(arr)+1):
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 
    if gender == 1 and i % nums == 0:
        if arr[i] == 1:
            arr[i] = 0
        elif arr[i] == 0:
            arr[i] = 1
            




# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
for j in range(1, len(arr)+1):
    # 여학생은 자기가 받은 수와 같은 번호
    if gender == 2 and j == nums:

        max_cnt = float('inf')
        cnt = 0

        # 스위치를 중심으로 좌우가 대칭이면서
        for d in range(2):
            for k in range(1, len(arr)):
                nj = j + dj[d] * k
                if 0 <= nj < len(arr):
                    cnt += 1
                    # 가장 많은 스위치를 포함하는 구간
                    # 스위치 홀수개
                    # 스위치의 상태 바꾸기
                    if cnt % 2 == 1 and max_cnt > cnt:
                        if arr[nj] == 1:
                            arr[nj] = 0

                        elif arr[nj] == 0:
                            arr[nj] = 1
'''

# ChatGPT의 도움을 받아 이해함

N = int(input())

arr = list(map(int, input().split()))

nums_student = int(input())

dj = [-1, 1]

for _ in range(nums_student):
    gender, nums = map(int, input().split())

    # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
    if gender == 1:
        for i in range(1, len(arr) + 1):
            if i % nums == 0:
                if arr[i - 1] == 1:
                    arr[i - 1] = 0
                elif arr[i - 1] == 0:
                    arr[i - 1] = 1

    # 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭인 가장 큰 구간을 찾는다.
    elif gender == 2:
        j = nums - 1   # 스위치 번호를 인덱스로 바꾸기

        left = j
        right = j

        # 좌우가 대칭인지 확인하면서 확장
        while left - 1 >= 0 and right + 1 < len(arr):
            if arr[left - 1] == arr[right + 1]:
                left -= 1
                right += 1
            else:
                break

        # 찾은 구간의 스위치 상태를 모두 바꾸기
        for k in range(left, right + 1):
            if arr[k] == 1:
                arr[k] = 0
            elif arr[k] == 0:
                arr[k] = 1

# 출력: 한 줄에 20개씩
for i in range(N):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
