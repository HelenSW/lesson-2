print('Привет! Сколько тебе лет?')
n = int(input())
def occupation(age):
 if(age<3):
  return ('Сидит дома с мамой')
 elif(age>=3 and age<7):
  return ('Ходит в садик')
 elif(age>=7 and age<=16):
  return ('Учится в школе')
 elif(age>16 and age<=23):
  return ('Учится в университете')
 elif(age>23 and age<=60):
  return ('Скорее всего вы еще работаете')
 else:
  return ('Вы на пенсии')
b=occupation(n)
print(b)
