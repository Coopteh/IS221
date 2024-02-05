# Пузырьковая сортировка (bubble sort)
Есть готовый код пузырьковой сортировки,  
класс O(n2) квадратичной скорости выполнения
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняются местами, если стоят в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
Использование  
```
my_list = [64, 64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print( ' '.join( map(str,sorted_list) ) )
```

### Задание (1 пара)
1) (1 пара) Измерьте время выполнения алгоритма сортировки, путем вычисления времени выполнения  
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
list1 = list(range(100))
list1.reverse()
list2 = list(range(100))
list2.reverse()
list3 = list(range(1000))
list3.reverse()
```
3) убедитесь что скорость вычисления O(n2)
