# Сортировка методом вставки
Код метода
```
def insert_value(L, value):
    ind = len(L) - 1
    ind_insert = 0
    while(ind >= 0):
        if (value > L[ind]):
            ind_insert = ind + 1
            ind = -1
        ind = ind - 1
    L.insert(ind_insert, value)
    return L

def insertion_sort(L):
    new_list = []
    while len(L) > 0:
        val = L.pop(0)
        new_list= insert_value(new_list, val)
    return new_list
```
Использование  
```
list1 = list(range(10))
list1.reverse()
print(list1)
new_list= insertion_sort(list1)
print(new_list)
```

### Задание
1) Измерьте время выполнения алгоритма сортировки, путем вычисления времени выполнения  
используя:
```
import time
start = time.time()
...
total = time.time() - start  # длительность выполнения
print("Время выполнения составило: ", total)
```
2) Проведите серию из 3 экспериментов для массивов из 10, 100, 1000 элементов
```
list2 = list(range(100))
list3 = list(range(1000))
```
3) какова скорость вычисления O(n) ?
