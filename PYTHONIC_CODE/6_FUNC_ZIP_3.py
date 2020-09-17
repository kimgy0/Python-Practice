#ZIP()함수는 1개 이상의 리스트값이 같은 인덱스에 있을 때 병렬로 묶는 함수이다.

alist=['a1','a2','a3']
blist=['b1','b2','b3']

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)