T = int(input()) # 테스트 케이스

for tc in range(1, T+1):

    odd_list = list(map(int, input().split())) # 리스트로 받기

    odd_sum = [] # 홀수 넣는 리스트 만들기
    total = 0 # 총합 구하기
    for i in odd_list:
        if i % 2 == 1: # 홀수인지 판별하기
            odd_sum.append(i) # 홀수이면 odd_sum 리스트에 넣기

            total += i # 홀수 값을 더해 총합 구하기


    print(f"#{tc} {total}")

