import re
st = "test date 31.8.2010 2.1.2021"
a = re.findall(r"\d{1,2}\.\d{1,2}\.\d{2,4}",st)
b = []
for i in range(len(a)):
  b = re.split(r'[.]', a[i])
  if (int(b[0])<=31)&(int(b[0])>=1)&(int(b[1])<=12)&(int(b[1])>=1):
    print(b[2]+"-"+b[1]+"-"+b[0])
