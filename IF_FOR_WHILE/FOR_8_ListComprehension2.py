#리스트 내포 사용하기
a=[1,2,3,4]
print("a =",a)
result=[num*3 for num in a if num % 2==0]
print("result =",result)