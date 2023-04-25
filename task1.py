from random import randint

n = int(input("Введите количество рандомных элементов в первом множестве "))
m = int(input("Введите количество рандомных элементов во втором множестве "))

SetN = set()
SetM = set()

for i in range(n):
    SetN.add(randint(1,30))

for i in range(m):
    SetM.add(randint(1,30))

result = SetN.intersection(SetM)

print(f" Первое множесто -> {SetN}, второе множество -> {SetM} ")

if result == set():
    print("Повторяющихся чисел не обнаружено")
else: print(f" Повторяющиеся числа -> {result} ")