import random

def start_game():
    print("Добро пожаловать в текстовый квест!")
    player_name = input("Как тебя зовут?\n")
    player_health = 100
    l = 1
    stats = {
        "имя": player_name,
        "здоровье": player_health,
        "уровень": l   
    }
    show_stats(stats)
    while True:
        first_choice(stats)
        show_stats(stats)
        if stats['здоровье'] <= 0:
            print("Вы проиграли. Игра окончена.")
            break
        if stats['уровень'] >= 10:
            print("Ты выиграл!")
            break
        continiue_game = input("")
        if continiue_game.lower() != 'да':
            print("Спасибо за игру! До новых встреч!")
            break    
def show_stats(stats):
    print (f"Имя: {stats['имя']}, Здоровье: {stats['здоровье']}, Уровень: {stats['уровень']}")
def encounter_dragon(stats):
    print("Ты встретил дракона!")
    action = input("Ты хочешь сражаться или убежать? (введите 'сражаться' или 'убежать') ")
    if action == "сражаться":
        if random.random() < 0.5:
            print("Ты победил дракона!")
            stats['уровень'] += 1
            stats['здоровье'] += randomrandint(5,15)
            print("Ты повысил свой уровень и восстановил здоровье!")
        else:
            damage = random.randint(10,30)
            stats['здоровье'] -= damage
            print(f"Дракон ранил тебя на {damage} здоровья!")
    else:
        print("Ты успешно убежал!")
def find_treasure(stats):
    treasure = random.choice(["золотые монеты", "магический артефакт", "древняя книга"])
    print(f"Ты нашёл {treasure}!")
    stats ['уровень'] += 1,
    stats ['здоровье'] += 5,
    print("Ты повысил уровень и восстановил немного здоровья!")
def first_choice(stats):
    choice = input("Ты стоишь на развилке. Пойти налево, направо или вперёд? (введите 'налево', 'направо','вперед')")
    if choice == random.choice(['налево','направо']):
        encounter_dragon(stats)
    elif choice == 'вперед':
        second_choice(stats)
    else:
        find_treasure(stats)    
def second_choice(stats):
    choice2 = input("Ты стоишь на развилке. Пойти налево или направо? (введите 'налево', 'направо')")
    if choice2 == random.choice(['налево','направо']):
        castle(stats)
    else:
        ovrag(stats)

def castle(stats):
    choicec = input("В замок ведёт закрытая дверь. Что делать? (попытаться открыть дверь или осмотреться)")
    if choicec == "попытаться открыть дверь":
        if random.random() < 0.5:
            print("Ты открыл дверь.")
            find_treasure(stats)
        else:
            choicec1 = input("Дверь не открылась. Может, есть что-нибудь рядом? (выбери исследовать или выйти)")
            if choicec1 == "исследовать":
                if random.random() < 0.2:
                    choiceghost = input("ПРИЗРАК!!! ЧТО ДЕЛАТЬ?! (бежать или остаться)")
                    if choiceghost == "остаться":
                        if random.random() < 0.5:
                            print("Призрак решил поделиться с вами своим жизненным опытом")
                            stats ['уровень'] += 3
                        else:
                            print("Он обезумел, пришлось защищаться.")
                            stats ['уровень'] += 1
                            stats ['здоровье'] += random.randint(10,20)
                    else:
                        first_choice(stats)
                else:
                    find_treasure(stats)
            else:
                first_choice(stats)
    else:
        encounter_dragon(stats)

def ovrag(stats):
    choiceovrag = input("Вы попали в Лесной овраг, можно осмотреться, а можно и отдохнуть")
    if choiceovrag == "осмотреться":
        if random.random() <= 0.3:
            print("Вы нашли полезные травы.")
            stats['здоровье'] += random.randint(10,30)
        else:
            print("Вы ничего не нашли.")
    else: 
        print ("Вы решили отдохнуть в овраге.")
        stats['здоровье'] += random.randint(5,15)
start_game()