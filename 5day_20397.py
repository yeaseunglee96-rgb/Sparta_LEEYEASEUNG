## ChatGPT의 도움을 받음 ##

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    stones = list(map(int, input().split()))

    for _ in range(M):
  
        i, j = map(int, input().split())

        center = i - 1

        # k = 1부터 j까지, 좌우 대칭으로 비교
        for k in range(1, j + 1):
            left = center - k
            right = center + k

            # 범위를 벗어나면 더 이상 진행하지 않고 중지
            if left < 0 or right >= N:
                break

            # 양쪽 돌 색이 같으면 둘 다 뒤집기
            if stones[left] == stones[right]:
                stones[left] = 1 - stones[left]     # 0->1, 1->0
                stones[right] = 1 - stones[right]


    print(f"#{tc}", *stones)