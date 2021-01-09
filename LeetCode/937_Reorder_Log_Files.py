def solution(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 동일한 문자에 대해서는 식별자로 순서를 정한다.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

answer = solution(logs)
print(answer)