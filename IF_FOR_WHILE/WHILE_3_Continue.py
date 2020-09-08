#continue를 이용해서 while의 맨처음으로 돌아가기
a=0
while a<10:
    a+=1
    if a%2==0:
        continue
    print(a)