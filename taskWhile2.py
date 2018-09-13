def ask_user():
 b={"Как дела?":"Хорошо!", "Что делаешь?":"Программирую","Где ты работаешь?":"В Москве", "Сколько времени у тебя сейчас?":"12"}
 while True:
  user_say=input('Задайте мне вопрос_')
  #print(user_say)
  #print(b[user_say])
  if user_say in b:
   print(user_say,b[user_say])
   break
  else:
   print('не знаю ответа')
ask_user()
