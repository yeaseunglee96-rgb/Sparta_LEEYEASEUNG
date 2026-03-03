# 문제 자체를 감시 받는 통로를 세는 것으로 착각하고 문제를 풀다보니 전혀 답이 나오지 않았다.
# 1번 문제를 풍선팡 문제와 동일하게 생각하고, 풀어나갔다. 그 의도대로 풀었다할지라도 k for문에서 범위 지정도 틀린 것을 오답하면서 확인했다.
# 2시간이 주어졌는데도 문제를 똑바로 읽지 않고 성급하게 풀다가 틀린 것이 너무 아쉬웠다.
# 외계인 문제도 IM 대비하면서 풀었었는데 너무 한심하다.
# 다음에는 이런 일이 없도록 문제를 잘 읽고 더 잘 준비하겠다.

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:

                for d in range(4):
                    for k in range(1, N):
                        ni = i + di[d] * k
                        nj = j + dj[d] * k

                        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0:
                            matrix[ni][nj] = 1
                        else:
                            break

    count = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 0:
                count += 1

    print(f"#{tc} {count}")

'''
T = int(input())

for tc in range(1, T+1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 통로 칸 수 세기
    count = 0
    for i in range(N):
        for j in range(N):
            # 술래 위치에서 시작
            if matrix[i][j] == 2:

                # 상하좌우 탐색
                for d in range(4):
                    for k in range(d):
                        ni = i + di[d] * k
                        nj = j + dj[d] * k

                        # ni, nj 범위 지정
                        if 0 <= ni < N and 0 <= nj < N:
                            # 벽을 만나지 않을 시
                            if matrix[ni][nj] != 1:
                                count += 1

    print(f"#{tc} {count}")
'''