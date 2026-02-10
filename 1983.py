# T = int(input())

# for tc in range(1, T+1):

#     N, K = map(int, input().split())

#     score = list(map(int, input().split()))

#     order = int(input())

#     total = 0
#     for i in score(a, b, c):
#         total = (a * 0.35) + (b * 0.45) + (c * 0.20)

#     print(total)
    

# 테스트케이스 개수 입력
T = int(input())

# 등급표 (문제에서 정해진 순서)
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

# 각 테스트케이스 처리
for tc in range(1, T + 1):
    
    # N : 전체 학생 수
    # K : 등급을 알고 싶은 학생 번호 (1번부터 시작)
    N, K = map(int, input().split())

    # 모든 학생의 총점을 저장할 리스트
    totals = []

    # K번째 학생의 총점을 따로 저장할 변수
    target_total = 0

    # 학생 번호는 1번부터 N번까지
    for student_idx in range(1, N + 1):

        # 각 학생의 점수 입력
        # a : 중간, b : 기말, c : 과제
        a, b, c = map(int, input().split())

        # 가중치 적용해서 총점 계산
        total = a * 0.35 + b * 0.45 + c * 0.20

        # 전체 총점 리스트에 저장
        totals.append(total)

        # 만약 현재 학생이 K번째 학생이면
        # 그 학생의 총점을 따로 기억해둔다
        if student_idx == K:
            target_total = total

    # 총점을 기준으로 내림차순 정렬 (높은 점수 → 앞쪽)
    totals.sort(reverse=True)

    # K번째 학생의 총점이 정렬된 리스트에서 몇 번째인지 찾기
    # (0부터 시작하는 인덱스)
    rank_idx = totals.index(target_total)

    # 한 등급당 몇 명씩 들어가는지 계산
    # 예: N=20이면 등급 10개 → 한 등급당 2명
    group_size = N // 10

    # 현재 순위가 몇 번째 등급 구간에 속하는지 계산
    # 예: rank_idx=3, group_size=2 → 3//2=1 → 두 번째 등급
    grade_idx = rank_idx // group_size

    # 해당 등급 출력
    print(f"#{tc} {grades[grade_idx]}")