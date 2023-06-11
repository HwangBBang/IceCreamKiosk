from Facade import *


if __name__ == "__main__":
    kiosk = KioskFacade(orderNumber = 3)
    # 첫번째 단계: TakeOut 또는 EatIn 선택 (전략 패턴)
    kiosk.printLine("Step 1: Order Type")
    kiosk.show_order_type()
    kiosk.select_order_type()
    
    # 두번째 단계: 사이즈 선택 (프로토타입 패턴)
    kiosk.printLine("Step 2: Size")
    kiosk.show_size()
    kiosk.select_size()
    kiosk.show_selected_size()

    # 세번째 단계: 메뉴 선택
    kiosk.printLine( "Step 3: Menu")
    kiosk.show_menu()
    kiosk.select_menu()

    # 네번째 단계: 이동 시간 선택
    kiosk.printLine("Step 4: TakeOut Time")
    kiosk.show_TakeOutTime()
    kiosk.select_TakeOutTime()

    # 다섯번째 단계: 선택 사항 보여주기
    kiosk.printLine("Step 5: Selections")
    kiosk.show_selections()


