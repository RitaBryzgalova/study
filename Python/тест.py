def print_check(items,discount):
    if discount < 0 or discount > 100:
        print('Ошибка')
        return
    print('Сумма оплаты')
    summ_items= sum(items)
    finel_discount = summ_items -(summ_items*discount/100)
    print(finel_discount)
    return finel_discount

items = [200,200]
print_check(items,1)
print_check(items,99)