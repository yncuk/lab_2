import re
def the_func() :
   st = input("Введите строку ")
   a = re.findall(r".", st)
   b = re.findall(r"\d", st)
   c = re.findall(r"[a-z]", st)
   d = re.findall(r"[A-Z]", st)
   e = re.findall(r"[.?!,]", st)
   if (len(a) >= 6)&(len(b) > 0)&(len(c) > 0)&(len(d) > 0)&(len(e) > 0):
     print("Пароль подходит по требованиям")
   else:
     print("Пароль не соответствует требованиям, введите новый пароль:")
     the_func()
the_func()
