def get_summ():
 try:
  num_one=int(input('Введите первое число'))
  num_two=int(input('Введите второе число'))
  summ=num_one+num_two
  print(summ)
 except ValueError:
  print('Ошибка')
get_summ()