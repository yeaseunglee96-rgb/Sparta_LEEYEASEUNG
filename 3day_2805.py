# 농장의 모든 합에서 마름모를 제외한 나머지 숫자를 제외하면, 마름모 안의 합을 구할 수 있다.
# 마름모 안의 대각선 길이는 N과 같다.
# 가로 세로의 중심으로부터 몇 칸 떨여졌는가?! 

### 강사님 힌트
# 2차원배열안의 어떤 칸(i,j) i행 j열에서 농작물을 수확하는지 하지 않는지 여부는
# 농장의 가운데 좌표 (N//2 , N//2) 에서 가로세로 합쳐서 N//2 칸 이하인지 아닌지를 검사하면 된다.
# 모든 위치를 순회하며 농장 가운데 칸과 가로세로 몇칸 떨어져있는지 계산하고, 칸수가 N//2 이하라면 농작물 수확!


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mid = N // 2  # 농장 중심 인덱스
    total = 0     # 수확한 농작물 총합

    # 모든 칸을 순회
    for i in range(N):
        for j in range(N):
            # 중심(mid, mid)으로부터의 맨해튼 거리(가로+세로 이동 거리)
            dist = abs(i - mid) + abs(j - mid)

            # 마름모 범위 안이면 수확
            if dist <= mid:
                total += farm[i][j]

    print(f"#{tc} {total}")