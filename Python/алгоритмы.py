#def binary_search(arr, target):
#    low = 0
#    high = len(arr) - 1#
#
#    while low <= high:
#        # Находим индекс среднего элемента
#        mid = (low + high) // 2
#        guess = arr[mid]

#        if guess == target:
#            return mid  # Элемент найден, возвращаем его индекс
#        if guess > target:
#            high = mid - 1  # Ищем в левой половине
#        else:
#            low = mid + 1   # Ищем в правой половине
#
#    return -1  # Элемент не найден

# Пример использования:
#my_list = [1, 3, 5, 7, 9]
#print(binary_search(my_list, 9))  
#print(binary_search(my_list, 1)) 


#def findSmallest(arr):
#    smallest = arr[0]
#    smallest_index = 0
#    for i in range(1,len(arr)):
#        if arr[i] < smallest:
#            smallest = arr[i]
#            smallest_index = i
#    return smallest_index
#
#def selectionSort(arr):
#    newArr = []
#    copiedArr = list(arr)
#    for i in range(len(copiedArr)):
#        smallest = findSmallest(copiedArr)
#       newArr.append(copiedArr.pop(smallest))
#    return newArr
#
#print(selectionSort([5,3,6,2,10]))


#def look_for_key(main_box):
#    pile = main_box.make_a_pile_to_look_through()
#    while pile is not empty:
#        box = pile.grab_a_box()
#        for item in box:
#            if item.is_a_box():
#                pile.append(item)
#            elif item.is_a_key():
#              print('Foun you key!')


#def look_for_key(box):
#    for item in box:
#        if item.is_a_box():
#            look_for_key(item)
#        elif item.is_a_key():
#           print('found the key!')


#def coutdown(i):
#    print(i)
#    if i <= 1:
#        return
#    else:
#        coutdown(i-1)
#coutdown(3)


#def fact(x):
#    if x == 1:
#        return 1
#    else:
#        return x * fact(x - 1)
#    
#a = fact(5)
#print(a)

#arr = [2,4,6]
#if arr == []:
#    print('Базовый случай')
#else:
#    print(sum(arr))

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

x =[2,4,6]
sum(x)