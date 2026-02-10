T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 L이 더 긴 배열, S가 더 짧은 배열이 되도록 맞춤
    if N >= M:
        L, S = A, B
    else:
        L, S = B, A

    max_sum = 0  # 충분히 작은 값으로 시작

    # L 위에서 S를 움직일 수 있는 시작 위치
    for start in range(len(L) - len(S) + 1):
        cur = 0
        # 한 위치에서 내적 계산
        for i in range(len(S)):
            cur += S[i] * L[start + i]
        max_sum = max(max_sum, cur)

    print(f"#{tc} {max_sum}")