class Person(): #sınıf tanımlaması
    def __init__(self,fname,lname): #yapıcı metod
        self.fname = fname
        self.lname = lname
        print('Person Created') # yapıcı metod sınıftan obje oluşunca otomatik çalışır

    def who_am_i(self): # sınıf metodu
        print('I am a Person')
    
    def eat(self):#sınıf metodu
        print('I am Eating')

class Student(Person): # Peron classından türedi
    def __init__(self,fname,lname,number): #yapıcı metod
        Person.__init__(self,fname,lname) # süper sınıfın yapıcı metodunu çağırıyor. super().__init__(self,fname,lname) de olabilirdi
        print('Stdent Created')
        self.studentNumber = number # obje atrribute
    
    #Overriding
    #süper sınıfta aynı isimde metod olduğu için bu metod onu ezer
    def who_am_i(self):
        print('I am a student')
    
    #object method
    def sayHello(self):
        print('Hello i am a student')

person = Person('aykut','B')
student = Student('ömer','B',1299)

person.who_am_i()
student.who_am_i()
person.eat()
student.eat()
student.sayHello()