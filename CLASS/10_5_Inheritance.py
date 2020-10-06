from CLASS.Inheritance import Person

class Employee(Person):
    def __init__(self,name,age,gender,salary,hire_date):
        super().__init__(name,age,gender)
        self.salary=salary
        self.hire_date=hire_date

    def __str__(self):
        return "열심히 일을 한다."
        #print("열심히 일을 한다.")

    def about_me(self):
        super().about_me()
        print("제 급여는 {0} 원이고, 제 입사일은 {1} 입니다.".format(self.salary,self.hire_date))

Student=Employee("김규영",23,"남자",0,"2017년3월")
f_person=Person("김규영",23,"남자")

f_person.about_me()
Student.about_me()

print(Student)

