T = int(input())

for tc in range(1, T+1):
    
    N = int(input())

    arr = list(map(int, input().split()))

    # 딕셔너리로 만들어서 각 수마다 개수 기입하기
    numbers_dict = {}
    for numbers in arr:
        if numbers in numbers_dict:
            numbers_dict[numbers] += 1
        else:
            numbers_dict[numbers] = 1

    # 딕셔너리에서 value 값만 도출
    number_value = numbers_dict.values()
    # 딕셔너리에서 value 값을 리스트화
    number_list = list(number_value)

    # 최빈수 값 구하기
    mode_number = 0 
    for i in number_list:
        if mode_number < i:
            mode_number = i
                
    answer = 0 # answer에 최빈수 key 값 출력하기
    for key, value in numbers_dict.items(): # 딕셔너리에서 key, value 값 도출
        if value == mode_number:
            if key > answer: # 단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라
                answer = key

    print(f"#{tc} {answer}")

    # 이 문제를 푸는 데 1시간 30분이 소요되었다. 90% 온전히 나의 힘으로 풀었는데,
    # for문 들여쓰기가 아직 취약하고, 
    # 마지막 최빈 수 여러 개일 경우 가장 큰 점수를 출력하라는 부분에서 쉽게 해결하지 못했다. 

