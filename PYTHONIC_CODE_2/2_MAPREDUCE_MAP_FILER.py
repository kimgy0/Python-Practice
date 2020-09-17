#맵 함수의 필터링 기능
#리스트 컴프리헨션 처럼 가능.

ex=[1,2,3,4,5]
print(list(map(lambda x:x**2 if x%2 == 0 else x, ex)))

print([x ** 2 if x%2==0 else x for x in ex])
#더 짧기 때문에 리스트 컴프리헨션
#r에 능숙한 사람은 위것을 더 쓸것같다.