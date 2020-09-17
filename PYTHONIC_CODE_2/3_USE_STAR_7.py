def asterisk_test(a,b,c,d,):
    print(a,b,c,d)
data={'b':1,'c':2,'d':3}
print(asterisk_test(10,**data))

#data에 키값에 asterisk_test의 인자인 b c d 가 없으면 안들어가진다.
#**로 딕셔너리를 언패킹해서 일반 정수형으로 바꿔줌. (value값만) (키값은 없어짐)