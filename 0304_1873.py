### 1시간 30분 넘게 고민을 하다가 조건문들을 어떻게 구현을 시킬지 몰라 결국 ChatGPT의 도움을 받았습니다.
### 포탄 발사에 대해서도 코드로 적용 될 줄 알았는데, 해당 코드는 구현이 되어 있지 않은 것 같아 의아했습니다.
### ChatGPT가 작성한 코드를 보고 계속 공부해야 할 것 같습니다.

### 내가 짠 코드 ###
'''
T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    H = input()

    N = int(input())
    arr = input()

    str_dict = {
        "." = 0,
        "*" = 1,
        "#" = 2,
        "-" = 3,
        "^" = 4,
        "v" = 5,
        "<" = 6,
        ">" = 7
    }

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    matrix = [list(map(str, input())) for _ in range(W)]

    board = [[0] * N for _ in range(N)]

    for i in range(H):
        for j in range(W):

            for d in range(4):
                for k in range(1, H):

                    ni = i + di[d] * k
                    nj = j + dj[d] * k

                    if not (0 <= ni < H and 0 <= nj < W):
                        break

                    # 포탄 부딪히면 벽돌 벽이 평이로 바뀜
                    if matrix[ni][nj] == "*":
                        matrix[ni][nj] = "."

                    elif matrix[ni][nj] == "#":
                        matrix[ni][nj] = "#"

### 방향 탐색 후 이동에 대해서 문자와 동일할 시 방향 이동에 2차원배열로 다시 다 설정해야 되는 건지 의문이 생겼고, 너무 비효율적인 것 같아 다른 방법을 모색하다가 멈추었습니다.
                    # if arr == U:
                    #     if board[]

                    # elif arr == D:

                    # elif arr == L:
                    
                    # elif arr == R:

                    # elif arr == S:
'''
### ChatGPT 코드 ###

T = int(input())

# 방향 매핑
dir_map = {
    '^': 0, 'v': 1, '<': 2, '>': 3
}
dir_char = ['^', 'v', '<', '>']
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

cmd_to_dir = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3
}

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    field = [list(input().strip()) for _ in range(H)]

    # 전차 위치/방향 찾기
    ti = tj = td = -1
    for i in range(H):
        for j in range(W):
            if field[i][j] in dir_map:
                ti, tj = i, j
                td = dir_map[field[i][j]]
                break
        if td != -1:
            break

    N = int(input())
    commands = input().strip()

    for c in commands:
        if c in cmd_to_dir:
            # 1) 방향 전환
            td = cmd_to_dir[c]
            field[ti][tj] = dir_char[td]

            # 2) 이동 가능하면 이동 (다음 칸이 평지 '.' 일 때만)
            ni = ti + di[td]
            nj = tj + dj[td]
            if 0 <= ni < H and 0 <= nj < W and field[ni][nj] == '.':
                field[ti][tj] = '.'
                ti, tj = ni, nj
                field[ti][tj] = dir_char[td]

        else:  # 'S'
            si = ti
            sj = tj
            while True:
                si += di[td]
                sj += dj[td]

                # 맵 밖이면 종료
                if not (0 <= si < H and 0 <= sj < W):
                    break

                # 벽돌/강철 만나면 처리 후 종료
                if field[si][sj] == '*':
                    field[si][sj] = '.'
                    break
                elif field[si][sj] == '#':
                    break
                # '.', '-', 전차문자(원래 전차는 한 대뿐이라 사실상 안 만남)는 그냥 계속 진행

    print(f"#{tc}", end=" ")
    for row in field:
        print("".join(row))