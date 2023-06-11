# 팩토리 메서드 - 
class Size():
    def __init__(self, orderNumber):
        self.orderNumber = orderNumber
        self.selectNum = None
        self.basketSize = None
        self.weight = None
        self.price = None

    def display_info(self):
        print(f"           Order Number: No.{self.orderNumber}\n")
        print(f"           Basket Size: {self.basketSize}\n")
        print(f"           Weight: {self.weight}g\n")
        print(f"           Price: {self.price}원\n")


class SizeFactory():
    def create_size(self, orderNumber, selectNum):
        if selectNum == 1:
            return SingleSize(orderNumber)
        elif selectNum == 2:
            return DoubleSize(orderNumber)
        elif selectNum == 3:
            return PintSize(orderNumber)
        elif selectNum == 4:
            return QuartSize(orderNumber)
        elif selectNum == 5:
            return FamilySize(orderNumber)
        elif selectNum == 6:
            return HalfGallonSize(orderNumber)
        else:
            print("           Invalid selectNum value. Please choose a valid option.\n")
            selectNum = int(input("           Enter your choice: "))
            return self.create_size(orderNumber, selectNum)


class SingleSize(Size):
    def __init__(self, orderNumber):
        super().__init__(orderNumber)
        self.selectNum = 1
        self.basketSize = "small"
        self.weight = 115
        self.price = 3500


class DoubleSize(Size):
    def __init__(self, orderNumber):
        super().__init__(orderNumber)
        self.selectNum = 2
        self.basketSize = "small"
        self.weight = 230
        self.price = 6700


class PintSize(Size):
    def __init__(self, orderNumber):
        super().__init__(orderNumber)
        self.selectNum = 3
        self.basketSize = "medium"
        self.weight = 320
        self.price = 8900


class QuartSize(Size):
    def __init__(self, orderNumber):
        super().__init__(orderNumber)
        self.selectNum = 4
        self.basketSize = "large"
        self.weight = 620
        self.price = 17000


class FamilySize(Size):
    def __init__(self, orderNumber):
        super().__init__(orderNumber)
        self.selectNum = 5
        self.basketSize = "xlarge"
        self.weight = 960
        self.price = 24000


class HalfGallonSize(Size):
    def __init__(self, orderNumber):
        super().__init__(orderNumber)
        self.selectNum = 6
        self.basketSize = "xlarge"
        self.weight = 1200
        self.price = 29000


# 팩토리 메서드 패턴을 선택한 이유는 다음과 같습니다:

# 유연성: 팩토리 메서드 패턴을 사용하면 객체 생성 로직을 추상화할 수 있습니다. 이는 코드의 유연성을 높여줍니다. 새로운 Size 서브클래스를 추가하거나 객체 생성 방식을 변경해야 할 경우, 팩토리 메서드를 수정하면 되므로 기존 코드의 변경을 최소화할 수 있습니다.

# 중복 코드 제거: 팩토리 메서드를 사용하면 객체 생성 로직을 한 곳에 집중시킬 수 있습니다. 생성자를 각각의 클래스에 구현하는 대신, 팩토리 메서드 내에서 객체 생성 로직을 구현하므로 중복 코드를 피할 수 있습니다.

# 다형성 활용: 팩토리 메서드 패턴은 다형성을 적극적으로 활용할 수 있는 패턴입니다. Size 클래스를 상속받은 다양한 서브클래스들을 생성하기 위해 SizeFactory의 create_size 메서드를 호출하는 것으로 다형성을 이용할 수 있습니다.

# 테스트 용이성: 팩토리 메서드 패턴은 테스트하기 쉽습니다. 특정 객체의 생성 방식을 변경하려면 단순히 SizeFactory의 create_size 메서드를 모킹(mocking)하여 원하는 객체를 반환하도록 설정할 수 있습니다. 이를 통해 테스트할 때 의존성을 쉽게 제어할 수 있습니다.
