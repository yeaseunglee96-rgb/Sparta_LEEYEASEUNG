# 내가 짠 코드에서 ChatGPT의 도움을 조금 받음.
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    di = [-1, 1, 1, -1]
    dj = [-1, -1, 1, 1]

    answer = 0  # 후보지 개수

    for r in range(N):
        for c in range(M):
            lower_cnt = 0  # (r,c) 기준으로 낮은 이웃 개수

            # 상하좌우 4방향
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[r][c] > arr[nr][nc]:
                        lower_cnt += 1

            # 대각선 4방향
            for d in range(4):
                ni = r + di[d]
                nj = c + dj[d]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[r][c] > arr[ni][nj]:
                        lower_cnt += 1

            # 후보지 판정(한 칸당 1번만)
            if lower_cnt >= 4:
                answer += 1

    print(f"#{tc} {answer}")


# 내가 짠 코드
# T = int(input())

# for tc in range(1, T+1):

#     N, M = list(map(int, input().split()))

#     arr = [list(map(int, input().split())) for _ in range(N)]

#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     di = [-1, 1, 1, -1]
#     dj = [-1, -1, 1, 1]


#     count_rc = 0
#     for r in range(N):
#         for c in range(M):

#             for d in range(4):

#                 nr = r + dr[d]
#                 nc = c + dc[d]
#                 if 0 <= nr < N and 0 <= nc < M:

#                     if arr[r][c] > arr[nr][nc]:
#                         count_rc += 1

#     count_ij = 0
#     for i in range(N):
#         for j in range(M):
                
#             for d in range(4):

#                 ni = i + di[d]
#                 nj = j + dj[d]

#                 if 0 <= ni < N and 0 <= nj < M:

#                     if arr[i][j] > arr[ni][nj]:
#                         count_ij += 1

#     result = count_rc + count_ij

#     print(f"#{tc} {result}")


'''
3
3 5
2 3 1 8 9 
7 6 2 2 6 
5 7 3 8 7 
5 5
5 2 3 5 2 
5 5 8 4 5 
3 6 8 5 2 
8 2 3 3 3 
5 1 5 4 5 
5 8
8 7 2 5 2 4 3 1 
7 4 2 3 9 3 5 1 
5 7 6 2 2 7 9 6 
9 8 7 6 2 1 9 4 
1 9 4 9 2 3 5 2 
10 5
6 1 2 3 3 
5 2 4 6 9 
2 3 8 4 5 
4 9 7 4 3 
2 8 5 9 7 
6 1 8 7 4 
1 4 5 8 6 
5 6 2 8 5 
4 2 9 8 2 
1 9 9 6 9 
'''
    


