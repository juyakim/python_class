### 자동차 클래스 생성
class car:
    def __init__(self,model,color,speed):

    #속성: 모델, 색, 현재 속도 
        self.model=model
        self.color=color
        self.speed= speed
        
    #속도를 올려주는 accelerate 메소드
    def accelerate(self,value):
        self.speed+= value

    # 속도를 낮춰주는 brake 메소드
    def brake(self,value):
        self.speed-= value

    # 현재 속도를 리턴해주는 get_speed 메소드
    def get_speed(self):
        return self.speed