# 내가 짠 코드가 Fail이 떠서 ChatGPT의 도움을 받고 이해함.

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))

    time.sort()   # 손님 도착 시간을 빠른 순서대로 정렬

    answer = "Possible"

    for i in range(N):
        made = (time[i] // M) * K   # time[i]초까지 만들어진 붕어빵 수
        need = i + 1                # i번째 손님까지 총 필요한 붕어빵 수

        if made < need:
            answer = "Impossible"
            break

    print(f"#{tc} {answer}")

### 내가 짠 코드, Fail
# T = int(input())

# for tc in range(1, T+1):

#     N, M, K = list(map(int, input().split()))

#     time = list((map(int, input().split())))

#     time_cnt = 0
#     fish_cnt = 0
#     answer = "Impossible"
#     for i in range(N):
#         time_cnt += M

#         print(f"#{time_cnt}")

#         for j in range(N):
#             fish_cnt += 1

#             if time[j] <= time_cnt:
#                 if fish_cnt <= M * K:
#                     answer = "Possible"

            
#     print(f"#{tc} {answer}")



'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2
'''
          


