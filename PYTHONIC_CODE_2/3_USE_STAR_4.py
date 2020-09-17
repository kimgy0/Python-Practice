def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

print(asterisk_test(1,*(2,3,4,5,6,7)))
#print 안에서 *로 튜플을 언패킹해버리고 함수에 넣는 순간 *로 다시 패킹되어서
#print로 출력하면 1,(2,3,4,5,6,7) 이런식으로 된다.
