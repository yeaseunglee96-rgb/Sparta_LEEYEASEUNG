T = int(input())

for tc in range(1, T+1):

    N = int(input())

    # 2차원 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 괴물 위치 찾기
    for i in range(N):
        for j in range(N):
            # 2(괴물위치)를 발견하면 해당 위치를 시작 지점으로 변경
            if matrix[i][j] == 2:
                si = i
                sj = j

    # 괴물 위치에서 상하좌우로 레이저 발사
    for d in range(4):
        ni = si + di[d]
        nj = sj + dj[d]

        # 벽을 만나거나 범위 밖으로 나갈 때까지 계속 레이저 전진
        while 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 1:
            if matrix[ni][nj] == 0:
                matrix[ni][nj] = -1 # 레이저 닿은 영역을 -1로 표기(0만 아니면 상관 없음)

            # 다음 칸으로 이동
            ni += di[d]
            nj += dj[d]

    # 0(빈칸) 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                cnt += 1

    
    print(f"#{tc} {cnt}")
    
# T = int(input())

# for tc in range(1, T+1):

#     N = int(input())

#     matrix = [list(map(int, input().split())) for _ in range(N)]

#     board = [[0] * N for _ in range(N)]

#     di = [-1, 1, 0, 0]
#     dj = [0, 0, -1, 1]

#     cnt = 0 

#     for i in range(N):
#         for j in range(N):

#             if matrix[i][j] == 2:
#                 for d in range(4):
#                     ni = i + di[d]
#                     nj = j + dj[d]

#                     if 0 <= ni < N and 0 <= nj < N:
#                         if matrix[ni][nj] == 0:
#                             matrix[ni][nj] = 1

#             if matrix[i][j] == 0:
#                 cnt += 1

#     print(f"#{tc} {cnt}")