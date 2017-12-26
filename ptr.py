
#Урок 1 переменные 19.12.17

# print('hello world')
# print('hello world')
# print( ' "it academy" ' )

# print('10+7=', 10+7)

# a=2
# b=3
# sum=a+b
# mul=a*b
# div=a/b
# sub=a-b
# mod =a%b

# print('sum =a+b ',sum )
# print('mul =a*b ',mul )
# print('div =a/b ',div )
# print('sub =a-b ',sub )
#---------------------------------

#Урок 2 21.12.17

# a =5
# b=4
# if a <b:
# 	print('oe')
# else:
# 	print('ro')


#  anton = 500;
# a  =1000;
# x = a + anton;
# print('x')

#--------------------------
#a=7
#b=4
#c=a-b
#print(a,'-'b, '=', a -b )

#print(f'{a}-{b}={c}')
#print('{0}-{1}={2}'.format(a,b,c))
#print('{a}+{b}={sum}'.format(a=2,b=7,sum=2+7))
#__________________________
# a=10
# b=5
# print('lol'a > b )
# print('aa lol'a > b)
# print('you are lol'a >= b)
# print('you are super lol'a <= b)
# print('you are super puper lol'a == b)
# print('you are super puper luper lol'a != b)
# __________________________________________
# x=True
# y=False
# z=True
# print('x is true', x is True)
# print('x is not true', x is not y)
# print(x is z)
# ____________________________________

# a =5
# b=4
# if a <b:
# 	print('oe')
# else:
# 	if 5>6 :
# 		print('5')
# 	else:
# 		print('6')
# 		print('oxoxoxox')

# a=10
# b=5
# if a<12 and a >3:
#  	print('kaka')
# if a<3 or a>5:
#  	print('b==a')
# for i in range (9,,-9):
# 	print(i)
# --------------------------------- 25.12.17

# a =0
# if(a==0)
# 	print('ты ввел 0' ) 
# if(a%2==0)
# 	print('четное')
# else
# 	print('нечетное')
# i = 0
# for i in range(1500,2700):
# 	if i%3 == 0:
# 		if i%5 == 0:
# 			print(i)

for a in range(1500, 2700):
	if (a%7==0) and (a%5==0):
		print (a)
# ________________________
o=0
f=5
while o<f:
	print("*"*o)
	o+=1
	if o==f:
		while o>0:
			print("*"*(o))
			o-=1
			if o==0:
				break
		break


# i = 0

# while i<5:
# 	print("*"*i)
# 	i+=1
# 	if i==5:
# 		while i>0:
# 			print("*"*(i))
# 			i-=1
# 			if i==0:
# 				break
# 		break

# a=[0,1,2,3,4,5,'text',-22,True,'hhhh' ]
# empty_list=[]
# b=[
# [0,1,2,3,4,5],
# [6,7,8,9,10],
# ]
# new_list=list()
# print(a)
# print('empty list',empty_list)
# print('b',b)
# print('new_list', new_list)

# a=[0,1,2,3,4,5,-22]
# res =0
# for i in a:
# 	res=res+i
# print('res:{}'. format(res))
# print('length of list "A"is:',len(a))
# print(a[6])


# a=list()
# a.append(5)
# a.append(True)
# a.append(['',False])
# # for i in a:
# print(a)
# a.pop()
# print(a)
# b=[0,1,2,3,4,5,6]
# b.reverse()
# print(b)

# l=[0,1,2,3,4,5,6,7,8,9]
# print(l[-1])
# b=l[2:6]
# print(b)
# print(l[:4])

# a =list()
# for i in range(10):
# 	a.append(i)
# print(a)

# b=[ (i*3/7) for i in range(10)]
# print(b)

# c=[x for x in range(20) if x %2==0]
# print(c)
