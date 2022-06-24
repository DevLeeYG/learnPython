# -*- coding: utf-8 -*-
dic = {'name':'pay'}

print(dic['name'])

dic['age'] = 19

del dic['name']

print(dic)

sport = {1:'피겨스케이팅',2:'야구',3:'축구'}

bc = sport.keys()



h = {'name':'pey','phone':'01123','birth':'1118'}
dd = h.keys()

print(dd)

for k in h.keys():#k 객체안에서 key를 반복으로 넣는다
    print(k)

item = h.items()
print(item)

print(h.get('name'))