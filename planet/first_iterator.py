iterable_value = "program"
iterable_obj = iter(iterable_value)

flag = True
while flag:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break
