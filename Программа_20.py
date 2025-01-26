def fairies(*args):
    for frs in args:
        print("Феи:",frs)
fs = input("Введите имена фей через запятую:")
fairies(fs)

def troll (**kwargs):
    for name, power in kwargs.items():
        print (f"Тролль {name} имеет силу {power}")
troll ("Тралл" = "12","Трулл" = "13")

def count(nf, nt):
    return nf + nt
nf = len(fs)
nt = len(tnames)
totaln = count(nf, nt)