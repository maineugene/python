# 10. Даны два множества. Проверьте, является ли одно подмножеством другого.
set_1 = {'a','fld','s','d','f',5,'e',3}
set_2 = {'fld',5}
if set_2.issubset(set_1):
    print('set_2 is subset of set_1')
elif set_1.issubset(set_2):
    print('set_1 is subset of set_2')
else:
    print('no subset relation')
