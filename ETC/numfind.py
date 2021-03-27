# https://somjang.tistory.com/entry/%EC%8B%A4%EC%A0%9C-%EB%A9%B4%EC%A0%91-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%AC%B8%EC%A0%9C-Python
# 블로그 탐방 중, 면접 보시며 푸셨던 문제라고 한다
# 취준하는 입장이기에 나도 풀어봄, 쉬운 편이긴 한데 면접 자리에서 떨릴 듯

# 세 개의 리스트가 주어졌고, 세 개의 리스트 모두 공통되는 요소 찾기

a = [1, 3, 5, 7, 9, 13, 15]
b = [4, 5, 6, 8, 13]
c = [5, 8, 13, 19]

ans = []

min_list = min(a, b, c, key=len)

for i in min_list:
    if i in a and i in b:
        ans.append(i)

print(ans)


# 배열을 한 곳에 모아 뽑아 볼 수도 있을듯
# min_list = min(temp, key=lambda x: len(x))
