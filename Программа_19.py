def book_tickets():
    a = input("Введите название вашего города:")
    b = input("Выберите количество дней:")    
    print("Билеты забронированы на:",a,"На",b,"дней.")
def find_hotel():
    a = input("Введите название вашего города:")
    c = input("Введите количество звёзд:")    
    print("Гостиница найдена в:",a,"(Звёзд:",c,')')
def buy_souvenirs():
    a = input("Введите название вашего города:")
    d = input("Выберите сумму денег:")    
    print("Сувениры куплены в:",a,"(",d,"рублей)")
def travel_plan():
    print("1: Забронировать билеты")
    print("2: Найти гостиницу")
    print("3: Купить сувениры")
    print("4: Выход")
travel_plan()
p = int(input("Ваш выбор:"))
if p == 1:
    book_tickets()
elif p == 2:
    find_hotel()
elif p == 3:
    buy_souvenirs()
elif p == 4:
    print("Спасибо за использование нашей продукции.")