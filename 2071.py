T = int(input()) # 테스트 케이스

for tc in range(1, T+1):

    arr = list(map(int, input().split())) # 리스트로 받기

    # 평균을 구하기 위한 리스트 길이 구하기(원소 개수)
    count = 0 
    # 총합 구하기
    total = 0
    for i in arr:
        count += 1
        total += i

        # 총합에서 숫자 길이만큼 나누어 평균값 구하기
        result = round(float(total/count))

    print(f"#{tc} {result}")