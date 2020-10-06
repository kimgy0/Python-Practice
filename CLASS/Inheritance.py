class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def about_me(self): #__Str__ 도 재정의로 가능.
        print("저의 이름은 {0} 이고요, 제 나이는 {1} 살 입니다.".format(self.name,str(self.age)))

person_object=Person("김규영",23,"남자")
person_object.about_me()

