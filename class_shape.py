### Shape 클래스 생성
class Shape:
# get_area 메소드를 갖게 해주세요.
    def get_area(self): 
        pass

### Circle 클래스 (Shape를 상속) 
class Circle(Shape):
    # Circle은 radius 속성
    def __init__(self, radius):
        self.radius= radius
    # get_area 메소드
    def get_area(self):
        print(f"{self.radius}")
### Rectangle 클래스 (Shape를 상속)
class Rectangle(Shape):
    #length와 widht 속성 
    def __init__(self, length, widht):
        self.length=length
        self.widht=widht    
        # get_area 메소드
    def get_area(self):
        print(f"{self.length}와 {self.widht}")

        

        



