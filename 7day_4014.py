# 아직 이 정도 문제는 혼자 힘으로 풀 수 없어 아쉽다. 계속 공부해보자!

def can_build(line, X):

    """
    line : 한 줄(행 또는 열)의 높이 정보 리스트
    X    : 경사로 길이

    return True  -> 이 줄에 활주로를 건설할 수 있다
           False -> 건설 불가
    """

    N = len(line)

    # used[i] = True  라면, i번째 칸은 이미 경사로에 사용된 칸
    # 문제 조건: "동일한 셀에 두 개 이상의 경사로를 겹쳐서 사용할 수 없다"
    used = [False] * N

    # i는 "현재 칸"의 인덱스
    # 우리는 line[i] 와 line[i+1] 을 비교하면서 왼쪽 -> 오른쪽으로 진행한다.
    i = 0
    while i < N - 1:

        # (1) 높이가 같으면 경사로 없이도 이어지므로 그냥 다음 칸으로 이동
        if line[i] == line[i + 1]:
            i += 1
            continue

        # (2) 높이가 다르면, 그 차이를 구해서 오르막/내리막/불가능을 판정
        diff = line[i + 1] - line[i]

        # 높이 차가 1 또는 -1이 아니면 경사로로도 연결 불가 (차이가 2 이상)
        if diff not in (1, -1):
            return False


        # (3) 오르막: 다음 칸이 1 높다
        # 예) ... 2 2 2 3 ...
        # 경사로는 "낮은 쪽"에 설치해야 한다.
        # 즉, (i-X+1) ~ i 까지 X칸이 모두 같은 높이(현재 높이)여야 설치 가능
        if diff == 1:
            low_h = line[i]  # 낮은 높이(현재 칸 높이)

            # i부터 왼쪽으로 X칸 확인: i, i-1, ..., i-(X-1)
            for k in range(i, i - X, -1):
                # 범위를 벗어나면 경사로 설치 불가
                if k < 0:
                    return False

                # 1) 높이가 모두 low_h인지
                # 2) 이미 다른 경사로에 사용된 칸인지(겹침 금지)
                if line[k] != low_h or used[k]:
                    return False

            # 위 조건을 모두 통과하면, 해당 X칸에 경사로 설치(사용 처리)
            for k in range(i, i - X, -1):
                used[k] = True

            # 오르막 처리를 했으니 다음 비교로 이동
            i += 1


        # (4) 내리막: 다음 칸이 1 낮다
        # 예) ... 3 2 2 2 ...
        # 경사로는 "낮은 쪽"에 설치해야 한다.
        # 즉, (i+1) ~ (i+X) 까지 X칸이 모두 같은 높이(다음 칸 높이)여야 설치 가능
        else:  # diff == -1
            low_h = line[i + 1]  # 낮은 높이(다음 칸 높이)

            # i+1부터 오른쪽으로 X칸 확인: i+1, i+2, ..., i+X
            for k in range(i + 1, i + 1 + X):
                # 범위를 벗어나면 경사로 설치 불가
                if k >= N:
                    return False

                # 1) 높이가 모두 low_h인지
                # 2) 이미 다른 경사로에 사용된 칸인지(겹침 금지)
                if line[k] != low_h or used[k]:
                    return False

            # 위 조건을 모두 통과하면, 해당 X칸에 경사로 설치(사용 처리)
            for k in range(i + 1, i + 1 + X):
                used[k] = True

            # 내리막은 "경사로 설치한 구간"은 이미 조건을 확인했으므로
            # 그 구간 끝 다음부터 다시 비교하면 된다.
            # i를 i+X로 점프하면, 다음 비교는 (i+X) 와 (i+X+1)
            i += X

    # 끝까지 문제가 없으면 활주로 설치 가능
    return True

T = int(input())

for tc in range(1, T + 1):
    # N: 지도 크기 (N*N), X: 경사로 길이
    N, X = map(int, input().split())

    # 지형 높이 정보
    board = [list(map(int, input().split())) for _ in range(N)]

    # 정답: 건설 가능한 "행 + 열" 개수
    ans = 0

    # 모든 행 검사
    for r in range(N):
        # board[r] 은 r번째 행(리스트)
        if can_build(board[r], X):
            ans += 1

    # 모든 열 검사
    for c in range(N):
        # c번째 열을 리스트로 만들어 검사
        col = [board[r][c] for r in range(N)]

        if can_build(col, X):
            ans += 1

    print(f"#{tc} {ans}")