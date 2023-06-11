from FactoryMethod import *
from Strategy import *
flavorName = [
    "루나 치즈케이크",
    "엄마는 외계인",
    "오레오 쿠키 앤 크림치즈",
    "아몬드 봉봉",
    "민트 초콜릿 칩",
    "슈팅스타",
    "초코나무 숲",
    "뉴욕 치즈케이크",
    "피스타치오 아몬드",
    "베리베리 스트로베리",
    "바람과 함께 사라지다",
    "레인보우 샤베트",
    "자모카 아몬드 훠지",
    "초콜릿 무스",
    "이상한 나라의 솜사탕",
    "초콜릿",
    "사과나라 헬로키티",
    "구름 속 시나몬 롤",
    "아이스 카멜 커피",
    "복숭아로 피치 올려",
    "블랙 슈가 밤",
    "애플 민트",
    "러브미",
    "벅스 버니버니 당근당근",
    "블랙 소르베",
    "사랑에 빠진 딸기",
    "핑크스푼 비긴즈",
    "초코넛 마카다미아",
    "오레오 쿠키 앤 크림",
    "월넛",
    "체리쥬빌레",
    "초코 체리쥬빌레",]

# 퍼사드 패턴 - 단계별로 호출을 추상화하여 간단한 인터페이스 제공
class KioskFacade:
    
    def __init__(self, orderNumber):
        self.strategy = None
        self.take_out_time = None
        self.size = None
        self.mySelected = []
        self.orderNumber = orderNumber

    def printLine(self, title):
        if title == "Step 4: TakeOut Time":
            if isinstance(self.strategy, TakeOutStrategy):
                print(f"\n ########################################  {title}  ############################################### \n")
            else:
                pass
        else:
            print(f"\n ########################################  {title}  ############################################### \n")
    
    def show_order_type(self):
        print("           Enter 1 for TakeOut or Enter 2 for EatIn")
        
    def select_order_type(self):
        print("           Enter your choice: ", end="");cmd = int(input())
        if cmd == 1:
            self.strategy = TakeOutStrategy()
            self.strategy.select_order_type()
        elif cmd == 2:
            self.strategy = EatInStrategy()
            self.strategy.select_order_type()
        else:
            print("           Invalid choice")
            return self.select_order_type()

        

    def show_size(self):
        print("""           Enter 1 for SingleSize     Enter 2 for DoubleSize""")
        print("""           Enter 3 for PintSize       Enter 4 for QuartSize """)
        print("""           Enter 5 for FamilySize     Enter 6 for HalfGallonSize\n""")
        
    def select_size(self):
        print("           Enter your choice: ", end="");cmd = int(input())
        self.size = SizeFactory().create_size(self.orderNumber,cmd)
        
    def show_selected_size(self):
        print(f"\n           Choice {self.size.__class__.__name__}")
        
    def show_menu(self):
        print(f"           Your SizeType is {self.size.__class__.__name__}, Choose {self.size.selectNum} menus")
        print("""
루나 치즈케이크     : 0          엄마는 외계인      : 1          오레오 쿠키 앤 크림치즈: 2         아몬드 봉봉           : 3               
민트 초콜릿 칩      : 4          슈팅스타           : 5          초코나무 숲            : 6         뉴욕 치즈케이크       : 7             
피스타치오 아몬드   : 8          베리베리 스트로베리: 9          바람과 함께 사라지다   : 10        레인보우 샤베트       : 11            
자모카 아몬드 훠지  : 12         초콜릿 무스        : 13         이상한 나라의 솜사탕   : 14        초콜릿                : 15                 
사과나라 헬로키티   : 16         구름 속 시나몬 롤  : 17         아이스 카멜 커피       : 18        복숭아로 피치 올려    : 19          
블랙 슈가 밤        : 20         애플 민트          : 21         러브미                 : 22        벅스 버니버니 당근당근: 23        
블랙 소르베         : 24         사랑에 빠진 딸기   : 25         핑크스푼 비긴즈        : 26        초코넛 마카다미아     : 27           
오레오 쿠키 앤 크림 : 28         월넛               : 29         체리쥬빌레             : 30        초코 체리쥬빌레       : 31            
        """)
        
    def select_menu(self):
        print("           Enter your choice: ", end="");cmd = int(input())
        if cmd < 0 or cmd > 31:
            print("           Invalid choice")
            return self.select_menu()
        else:
            self.mySelected.append(flavorName[cmd])
            print(f"           {flavorName[cmd]} is selected \n")
            
            if self.size.selectNum != len(self.mySelected):
                return self.select_menu()
    
    # 4. TakeOut Time 선택
    def show_TakeOutTime(self):
        if isinstance(self.strategy, TakeOutStrategy):
            print("           Enter 0 for 15min     Enter 1 for 30min")
            print("           Enter 2 for 1hour     Enter 3 for 2hour")
            
        else:
            pass
    def select_TakeOutTime(self):
        if isinstance(self.strategy, TakeOutStrategy):
            print("           Enter your choice: ", end="");cmd = int(input())
            if cmd == 0:
                print("\n           15min is selected \n")
                self.take_out_time = 15
            elif cmd == 1:
                print("\n           30min is selected \n")
                self.take_out_time = 30
            elif cmd == 2:
                print("\n           1hour is selected \n")
                self.take_out_time = 60
            elif cmd == 3:
                print("\n           2hour is selected \n")
                self.take_out_time = 120
            else:
                print("\n           Invalid choice")
                return self.select_TakeOutTime()                
        
    # 5. 선택한 결과 출력
    def show_selections(self):
        
        print(f"           Order Type: {self.strategy.__class__.__name__} \n")
        if isinstance(self.strategy, TakeOutStrategy): print(f"           TakeOut Time: {self.take_out_time}분 \n")
        print(f"           Size Type: {self.size.__class__.__name__} \n")
        self.size.display_info()
        print("           Menu: |" ,end=" ")
        for item in self.mySelected:
            print(item, end=" | ")
        print("\n")
