# 10844 문제를 풀며 생겼던 이슈
# 둘이 같은 array로 초기화 되는데 문제 해결후의 정답 값은 다르다
# 어디서 차이가 존재하는 걸까?

dp1 = [[0 for _ in range(10)] for _ in range(3)]
dp2 = [[0] * 10] * 10
dp3 = [[0] * 10 for _ in range(10)]

dp1[1][1] = 1
dp2[1][1] = 1
dp3[1][1] = 1

print(f'dp1 = {dp1}')
print(f'dp2 = {dp2}')
print(f'dp3 = {dp3}')
