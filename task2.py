print('ведите 2 строки')
str1=input()
str2=input()
def dif(s1,s2):
 if(s1.isdigit()==True or s2.isdigit()==True):
  return('0')
 elif(s1==s2):
  return('1')
 elif(len(s1)>len(s2)):
  return('2')
 elif(s2=='learn'):
  return('3')
a=dif(str1,str2)
print(a)