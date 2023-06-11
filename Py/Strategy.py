from abc import ABC, abstractmethod

# 전략 패턴 - TakeOut 또는 EatIn 선택에 대한 전략을 정의
class OrderStrategy(ABC):
    @abstractmethod
    # 추상 메소드
    def select_order_type(self):
        pass

class TakeOutStrategy(OrderStrategy):
    # 오버라이딩
    def select_order_type(self):
        print("           You Choice Take Out")

class EatInStrategy(OrderStrategy):
    # 오버라이딩
    def select_order_type(self):
        print("           You Choice Eat In")


