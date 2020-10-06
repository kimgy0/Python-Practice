class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
        #해당 자식 객체를 제외한 다른 클래스가 이 메서드를 쓰지 못하게 함.

class Dog(Animal):
    def talk(self):
        return "woof! woof!"
class Cat(Animal):
    def talk(self):
        return "meow!"

animals=[Cat("missy"),Dog("mistoffelees"),Cat("lassie")]

for animal in animals:
    print(animal.name,":",animal.talk())