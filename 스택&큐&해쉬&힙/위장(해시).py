from collections import defaultdict

def solution(clothes):

    answer = 1
    clothes_dict = defaultdict(int) # 딕셔너리 초기화
    
    # 딕셔너리에 의상 종류별 개수 카운트
    for c in clothes:
        clothes_dict[c[1]] += 1

        
    # 각 의상 종류별 개수에 +1을 하여 해당 의상을 입지 않은 경우의 수도 고려
    for cnt in clothes_dict.values():

        answer *= (cnt+1)
        
    # 모든 의상을 입지 않은 경우의 수 1을 빼줌
    return answer - 1
        
    