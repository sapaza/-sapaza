o = input()
z=int(o[0])
x=int(o[1])
c=int(o[2])
ITSATRAP = ("Ловушка!")
if z == 0:
    print(ITSATRAP)
elif x == 0:
    print(ITSATRAP)
elif c == 0:
    print(ITSATRAP)
else:
    A = "А"
    a = A * z
    B = "Б"
    b = B * x
    V = "В"
    v = V * c
    w = a + "" + b + "" + v
    print(w)