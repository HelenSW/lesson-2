print('Привет! Сколько тебе лет?')
n = int(input())
def occupation(age):
 if(age<3):
  print('Сидит дома с мамой')
 elif(age>=3 and age<7):
  print('Ходит в садик')
 elif(age>=7 and age<=16):
  print('Учится в школе')
 elif(age>16 and age<=23):
  print('Учится в университете')
 elif(age>23 and age<=60):
  print('Скорее всего вы еще работаете')
 else:
  print('Вы на пенсии')
occupation(n)
