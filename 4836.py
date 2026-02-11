T = int(input())

for tc in range(1, T+1):

    N = int(input())
    
    # 10x10 격자
    board = [[0] * 10 for _ in range(10)]

    for c in range(N):

        x1, y1, x2, y2, color = map(int, input().split())

        # 사각형 칠하기
        # 행 r 우선 순회
        for r in range(x1, x2 + 1):
            for c in range(y1, y2 + 1):
                # 같은 색 여러 번 칠하기 방지
                if board[r][c] == 0:
                    board[r][c] = color

                elif board[r][c] != color and board[r][c] != 3:
                    board[r][c] = 3

    # 보라색 칸 세기
    count = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                count += 1

    print(f"#{tc} {count}")