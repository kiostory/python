
MENU = {                          #중첩 dictionary
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {                   #원재료 보유량
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_make(order, tag):
    """make_an_order함수로부터 주문을 받아 남은 원재료로 만들 수 있는지 확인하고
    부족할 경우 태그를 false로 변경한다.
    process함수로부터 주문받은 메뉴만큼의 원재료를 차감한다.
    """
    global turnon
    if tag == "resource_check" :
        for i in MENU[order]["ingredients"] :
            if resources[i]-MENU[order]["ingredients"][i] < 0 :
                print(f"Sorry there is not enough {i}.")
                turnon = False

    elif tag == "make_it" :
        for i in MENU[order]["ingredients"] :
            resources[i] -= MENU[order]["ingredients"][i]

def report(i):
    """메뉴에 report가 입력되었을 때, 남은 원재료별 양과, 수입을 출력한다. income변수값을 인자로 받음"""
    print(f"\tWater: {resources['water']}ml")
    print(f"\tMilk: {resources['milk']}ml")
    print(f"\tCoffee: {resources['coffee']}g")
    print(f"\tMoney: ${i}")

def make_an_order(income):
    """주문과 커피머신의 계속사용여부를 global변수로 하고
    들어온 3가지 주문에 대해 원재료양을 체크하도록 전달하고
    히든 메뉴인 report를 처리하도록 전달하고 off를 처리한다.
    현재까지의 수입을 인자로 받고 report에 사용한다."""
    global order, turnon
    order = input(f"What would you like? ({Menu.get_items()}) :").lower()
    if order == "espresso" or order == "latte" or order == "cappuccino" :
        check_make(order, tag = "resource_check")
    elif order == "report" :
        report(income)
        make_an_order(income)
    elif order == "off":
        sys.exit()
    else :
        turnon = False   # 쓸데없이 process()를 수행하지 않도록 tagging

def process(income):
    """판매하는 메뉴가 아닐경우를 처리한다.
    판매하는 메뉴일 경우, 코인 종류별로 지불한 최종 금액을 계산하고,
    주문한 메뉴의 금액과 비교하여 주문을 받고 커피를 만들도록 전달하고, 잔돈을 내어주거나,
    부족할 경우 넣은 돈을 그대로 반환한다.
    income을 반환한다."""
    global turnon
    if order not in ("espresso", "latte", "cappuccino") :
        return 0
    print("Please insert coins.")
    total_money = int(input("\thow many quarters?: ")) * 0.25
    total_money += int(input("\thow many dimes?: ")) * 0.1
    total_money += int(input("\thow many nickles?: ")) * 0.05
    total_money += int(input("\thow many pennies?: ")) * 0.01
    if MENU[order]["cost"] <= total_money :
        income += MENU[order]["cost"]
        exchange = total_money - MENU[order]["cost"]
        if order == "espresso"  or order == "latte" or order == "cappuccino" :
            check_make(order, tag="make_it")
        if exchange > 0 :
            print(f"Here is ${round(exchange,2)} in change.")
        print(f"Here is your {order} ☕  Enjoy!")
    else :
        print("Sorry that's not enough money. Money refunded.")
    return income

import sys      # order가 off일 경우, 그 즉시 프로그램 종료를 위한 sys.exit() 함수를 사용하기 위함
income = 0      # 수입 적산을 위한 변수
turnon = True   # 반복적인 프로그램 실행을 위한 bool변수. off

while turnon :
    make_an_order(income)
    if turnon :             # 금액이 모자라거나, 메뉴 외에 주문일 경우 process를 거치지 않도록 함
        income = process(income)
    turnon = True   # 주문이 off가 아닌이상 계속하기 위한 tagging
