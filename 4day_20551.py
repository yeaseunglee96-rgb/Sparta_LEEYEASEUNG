T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    # C는 최대한 유지
    c = C
    # B는 c-1 이하로만 가능 (엄격 증가)
    b = min(B, c - 1)
    # A는 b-1 이하로만 가능
    a = min(A, b - 1)

    # a가 1 미만이면 (세 박스를 모두 1개 이상 + 엄격 증가) 불가능
    if a < 1:
        result = -1
    else:
        # 먹은 개수 = 원래 합 - 남긴 합
        result = (A + B + C) - (a + b + c)

    print(f"#{tc} {result}")


# 아래와 같은 방식으로 풀려고 하여 조건 먼저 세우려고 하였으나 코드가 진행이 되지 않았음
# 상자의 사탕을 비교하여 조건에 맞추어 하나씩 먹을 때마다 count를 1 증가시켜 개수를 세려고 하였음
# T = int(input())

# for tc in range(1, T+1):
        
#     A, B, C = map(int, input().split())

#     if A < B < C and A >= 1 and B >= 2 and C >= 3:
#         result = 1

#     elif A < 1 and B < 2 and C < 3:
#         result = 0

#     print(f"#{tc} {result}")
    

'''
4
3 2 1
1 2 3
3 5 5
5 6 6
'''