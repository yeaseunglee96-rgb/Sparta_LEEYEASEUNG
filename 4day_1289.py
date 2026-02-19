T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input()))

    result = 0
    cur = 0  # 현재 메모리 상태(초기값은 모두 0)

    for i in range(len(arr)):
        if arr[i] != cur:
            result += 1
            cur = arr[i]

    print(f"#{tc} {result}")

# i 기준으로 뒤 숫자와 다르면 result를 0으로 기록
# i 기준으로 뒤 숫자와 같고, i 기준으로 마지막 숫자와 동일하면 리스트 길이에서 i를 빼는 방식으로 구하려고 하였음


#### 내가 짠 코드 ####
# T = int(input())

# for tc in range(1, T+1):

#     arr = list(map(int, input()))

#     result = 0
#     for i in range(len(arr)):
#         if arr[i] != arr[i+1]:
#             result = 0

#         elif arr[i] == arr[i+1] and arr[i] == arr[len(arr)-1]:
#             result = len(arr) - i

#     print(f"#{tc} {result}")

#### ChatGPT 피드백 ####
# arr[i+1] 때문에 마지막 i에서 IndexError 나요. (i == len(arr)-1일 때 i+1 없음)
# result를 “바뀌면 0”처럼 계속 덮어써서 정답이 누적되지 않음
# 이 문제는 최소 수정 횟수 = “바뀌는 횟수”를 세어야 해요.
# elif arr[i] == arr[i+1] and arr[i] == arr[len(arr)-1] 이 조건은 문제의 규칙(선택한 비트부터 끝까지 덮어쓰기)과 직접적으로 연결되지 않아서 맞는 판정이 되기 어려워요.

    