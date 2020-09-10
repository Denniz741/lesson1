a = 2
b = 0.5
print(a+b)



name = 'Denis'
print(f"Привет , {name} !")



#v = int(input('Введите число от 1 до 10    '))
#print(int(v + 10))


#name = input("Введите Ваше имя   ")
#print(f'Привет, {name}. Как дела? ')


print(int(1.0))



a = [3 , 5 , 7 , 9 , 10.5]
print(a)
a.append("Python")
print(a)
del a[5]
print(a)



meteo = {'city' : 'Москва', 'temperature' : '20' }
print (meteo['city'])
meteo['temperature'] = str(int(meteo['temperature']) - 5)
print(meteo)

print(meteo.get('country'))

#print(meteo['country'])
meteo.get('country','Россия')
#print(meteo['country'])
meteo['date'] = '2020.09.10'

#meteo = {'city' : 'Москва', 'temperature' : '20',
 #   'country' }
print(meteo)
print(len(meteo))
