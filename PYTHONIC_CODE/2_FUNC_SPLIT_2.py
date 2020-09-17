#SPLIT() 함수의 매개변수를 넣어서 텍스트를 어떻게 분리하는지 알아보자.

example='pyhon,jquery,javascript'
result=example.split(",") #문자열을 리스트로 변환
print(result)

a,b,c=example.split(",")#튜플도 언패킹 가능
print(a,b,c)

example='theteamlab.univ.edu'
subdomain,domain,tld=example.split('.')
print(subdomain,domain,tld)