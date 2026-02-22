T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))  # 0: 흰색, 1: 검은색

    for _ in range(M):
        i, j = map(int, input().split())      # i, j는 1-indexed
        color = stones[i - 1]                 # i번째 돌의 "현재" 색
        end = min(N, i + j - 1)               # 덮어쓸 마지막 위치(1-indexed)

        for k in range(i - 1, end):           # 0-indexed 구간 [i-1, end-1]
            stones[k] = color

    print(f"#{tc}", *stones)