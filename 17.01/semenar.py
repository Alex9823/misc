#словари(dictionaty)
# чтобы создать пустой словарь keys are to the left ALWAYS
#значения могут быть любыми, одинаковыми ключи не могут быть 
#словарь это пары значений, поиск по ключам, ключи либо строки либо числа
d={'Элис': '12345','Боб':'1234'}
#чтобы извлечь инфу
print(d['Элис'])
d['Элис']='999'
#чтобы изменить
d['smth']='11'
#чтобы добавить
len(d)#3 
if 'Элис' in d:
    print (d['Элис'])
for key in d:
    print(key+ '*'+d[key])

#в отличие от массива словари не упорядочены и этот
#код может распечатывать все в разном порядке
#массивы из словаря

key=d.keys()#массив ключей
d.values() #массив значений
if '999' in d.values():
    print('yes')
sort(arr) #сорти
arr=[1,0,5,9]
arr2=sorted(arr)#он создает копию но массив остается


