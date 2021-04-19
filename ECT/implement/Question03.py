def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1
        # 슬라이싱할 때 string의 개수보다 크더라도 오류가 발생하지 않는다!
        # i == 8 인 경우
        # prev = c, s[8:9]를 비교하게 되는데 s[8:9]의 값은 '' 이다.
        # 하지만 s[8]을 비교하게 되면 out of range 오류가 발생한다!!!
        for i in range(step, len(s)+step, step):
            if prev == s[i:i + step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[i:i + step]
                cnt = 1

        answer = min(answer, len(compressed))

# 범위 range(step, len(s), step)인 경우
# 마지막 문자열이 prev = c 일 때 비교할 문자열이 없어 compressed에 문자열을
# 저장하지 않고 for문이 종료되므 남아있는 문자열을 처리해줘야 한다
'''
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1

        for i in range(step, len(s)+step, step):
            if prev == s[i:i + step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[i:i + step]
                cnt = 1로
        
        # 남아있는 문자열 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev

        answer = min(answer, len(compressed))
'''

solution("aabbaccc")