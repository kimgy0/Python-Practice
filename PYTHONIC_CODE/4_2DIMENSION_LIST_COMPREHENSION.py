#비슷한 방식으로 이차원 리스트를 만들 수 있다. 앞 중첩 반복문의 예시 코드 결과는 일차원 리스트였다.
#그렇다면 하나의 정보를 열 ROW단위로 저장하는 이차원 리스트는 어떻게 만들 수 있을까?

words='The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff=[[w.upper(),w.lower(),len(w)] for w in words]

for i in stuff:
    print(i)