#readline함수와는 다른 readlines함수로 여러줄을 읽어오자
f=open("newFile.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()
#이방법을 많이 씀.