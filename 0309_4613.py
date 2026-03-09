# 쉬운 당근 포장 방식으로 문제를 이해하고 풀다가 코드를 제대로 구현시키지 못해 도움을 구함
# 은서님의 코드를 먼저 보면서 더 간단하게 코드를 구성할 수 있을 거라 생각하고,
# visited 부분을 바로 cnt 개수를 세는 방식으로 변경함
# 코드 길이가 더 짧아져 코드를 이해하기 쉬워짐
# 아래 코드를 반복해서 작성하면서 숙지함 

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    result = float('inf')

    # w: 흰색 줄 수
    for w in range(1, N - 1):
        # b: 파란색 줄 수 
        for b in range(1, N - w):
            # r: 빨간색 줄 수
            r = N - w - b

            # 빨간색 줄도 최소 1줄은 있어야 함
            if r < 1:
                continue

            cnt = 0

            # 0 ~ w-1 행은 모두 W여야 함
            for i in range(w):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cnt += 1

            # w ~ w+b-1 행은 모두 B여야 함
            for i in range(w, w + b):
                for j in range(M):
                    if flag[i][j] != 'B':
                        cnt += 1

            # w+b ~ N-1 행은 모두 R여야 함
            for i in range(w + b, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cnt += 1

            result = min(result, cnt)

    print(f"#{tc} {result}")