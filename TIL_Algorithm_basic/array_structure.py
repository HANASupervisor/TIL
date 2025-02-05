'''
8 7
1 3 5 7 9 11 13 15

8 1
1 1 1 1 3 3 1 2
'''
################ 내 풀이 #################
cnt = 0
def calculate():
    global cnt
    n, k = map(int, input().split())
    element_array = list(map(int, input().split()))
    for i in element_array:
        if i == k:
            cnt += 1

    return cnt
print(calculate())
################ 고수의 풀이 ###############
def solution(n,A,k):
    answer = 0
    for a in A:
        if a == k:
            answer += 1
    return answer

n, k  = map(int, input().split())
A = list(map(int, input().split()))
print(solution(n,A,k))