### Animal 부모클래스 생성

class Animal: 
    
    #클래스 속성
    def __init__(self,name,age):
        self.name= name
        self.age= age
        
    # speak 메소드
    def speak(self):
        print(f'동물의 나이는 {self.name} 이고, 나이는 {self.age}살 입니다.')

### Dog 자식클래스 (Animal 상속)

class Dog(Animal): 
    
    #클래스 속성
    def __init__(self, name, age):
        super().__init__(name, age)
        
    # speak 메소드  
    def speak(self):
        print(f'강아지의 나이는 {self.name} 이고, 나이는 {self.age}살 입니다.')

### Cat 자식클래스 (Animal 상속)

class Cat(Animal):
    
    #클래스 속성
    def __init__(self, name, age):
        super().__init__(name, age)
        
    # speak 메소드
    def speak(self):
        print(f'고양이의 나이는 {self.name} 이고, 나이는 {self.age}살 입니다.')
