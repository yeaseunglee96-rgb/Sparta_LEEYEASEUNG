T = int(input())  # 테스트 케이스 개수 입력 받기

for tc in range(1, T + 1):
    N = int(input())

    # N = 2^a × 3^b × 5^c × 7^d × 11^e
    # 각 소인수(2,3,5,7,11)의 지수(a,b,c,d,e)를 저장할 리스트
    # cnt[0] = 2의 개수, cnt[1] = 3의 개수, ..., cnt[4] = 11의 개수
    cnt = [0] * 5

    # N = 2^a × 3^b × 5^c × 7^d × 11^e
    # 문제에서 주어진 소인수들
    prime = [2, 3, 5, 7, 11]

    # prime 리스트를 0~4까지 돌면서 각 소인수로 나눌 수 있는 만큼 나눈다
    for i in range(5):
        # N이 prime[i]로 나누어 떨어지는 동안 반복(=더 이상 못 나눌 때까지)
        while N % prime[i] == 0:
            N //= prime[i]   # N을 해당 소인수로 한 번 나눈 몫으로 갱신
            cnt[i] += 1      # 해당 소인수의 개수(지수)를 1 증가

    # 출력 형식: #tc a b c d e
    # *cnt는 리스트를 풀어서(언패킹) 값들을 공백으로 출력하게 해준다
    print(f"#{tc}", *cnt)


# 처음에는 2로 나눠지는 값들을 리스트에 넣어 그 리스트의 개수를 세는 방식으로 답을 도출하려고 했다.
# 하지만 코드가 잘 구현되지 않아 ChatGPT에게 물어보았는데,
# 이 방식은 너무 비효율적이라 나눠지는 것을 반복할 때마다 횟수를 세는 방식으로 변경하여 문제를 풀어갔다. 

# numbers = 6791400
# numbers_list = []
# count = 0
# for i in numbers:
#     while numbers % 2 == 0:
#         numbers_list.append(i)
#         count += 1

