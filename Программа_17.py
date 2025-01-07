school = {"Аня", "Вася", "Катя", "Дима"}
club = {"Аня", "Вася", "Петя", "Маша"} 
common = school & club
school_only = school - club
club_only = club - school
all_friends = school | club
school.add ("Саша")
club.remove ("Петя")
print("Общие друзья: ", common)
print("Друзья только по школе: ", school_only )
print("Друзья только по кружку: ", club_only)
print("Все друзья: ", all_friends)
print("Друзья по школе с Сашей: ", school)
print("Друзья по кружку без Пети: ", club)