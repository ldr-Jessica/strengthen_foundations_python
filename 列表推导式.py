a=[1,2,3,4,5]
#把a变成[2,4,6,8,10]
#正常的for循环
l=[]
for i in a:
    i+=i
    l.append(i)
print(l)

#列表推导式
b=[2*m for m in a]
#python里面的乘法运算一定不能省略乘号，否则会被当成虚数处理或者报错
#列表推导式前面的结果不用写变量等于，直接写新的结果是啥
print(b)

c=[2,3,4,5,6]
d=[1,3,5,7,9]
#想要c+d
l1=[t+n for t,n in zip(c,d)]
print(l1)

#判断奇数偶数
l2=[]
for i in range(1,11):
    if i%2==0:
        l2.append(i)
print(l2)

#for if(列表推导式）
f=[w for w in range(1,11) if w%2==0]

#if for(三元运算)
l4=["偶数" if h%2==0 else "奇数" for h in range(1,11)]
print(l4)

#练习：三元运算和列表推导式的区分

#练习1:一批商品价格 [10, 50, 120, 200, 35]，满 100 打八折，不满 100 原价。
p=[10, 50, 120, 200, 35]
p2=[y*0.8 if y>=100 else y for y in p]
print(p2)

#练习2：一批分数 [85, 42, 90, 55, 76, 30]，≥90 是 "A"，≥60 是 "B"，其余 "C"
score=[85, 42, 90, 55, 76, 30]
s1=["A" if r>=90 else "C" if r<60 else "B" for r in score]
print(s1)

'''
总结：在列表的编程中，列表推导式是从原来的列表里面
筛选出符合条件的元素并加工之后放到一个新列表，
三元运算是对原来列表的元素进行条件判断和定性
'''

'''
练习3：
一批用户名 ["Alice", "BOB", "charlie", "DAVE"]，
全大写或全小写的转成首字母大写，混合大小写的保持不变。
'''
names = ["Alice", "BOB", "charlie", "DAVE"]
result = [n.title() if n.isupper() or n.islower() else n for n in names]
print(result)
#n.title()  字符串的首字母大写函数

#一批气温 [35, 28, 40, 15, 38, 22]，≥38 标 "高温"，≤15 标 "低温"，其余标 "正常"
temp=[35, 28, 40, 15, 38, 22]
r=["高温" if k>=38 else "低温" if k<=15 else "正常" for k in temp]
print(r)

'''
一批包裹重量（kg）[0.5, 3, 8, 12, 0.3, 5, 15]，
运费规则：≤1kg 收 8 元，1~10kg 收 15 元，>10kg 收 25 元。
输出每个包裹的运费列表。
'''
weight=[0.5, 3, 8, 12, 0.3, 5, 15]
price=[8 if q<=1 else 25 if q>10 else 15 for q in weight]
print(price)

'''
给定分数列表 [85, 42, 90, 55, 76, 30, 100, 60]，要求：
先筛选出 ≥60 的分数
再对筛选后的分数评级：≥90 标 "A"，其余标 "B"
最终输出评级列表
'''
s=[85, 42, 90, 55, 76, 30, 100, 60]
ts=[i for i in s if i>=60]
ns=["A" if v>=90 else "B" for v in ts]
#字典表达式{键表达式: 值表达式 for 变量 in 可迭代对象}
dic={i:j for i,j in zip(ns,ts)}
print(dic)

d={"Jessie":85,"Tom":42,"Amy":90,"Jack":55,"Jessica":100}
d1={"成绩及格的人和分数有":{m:n for m,n in d.items() if n>=60}}
print(d1)
for k,v in d1.items():
    s1=[f"{m}的等级是A，分数为{n}" for m,n in v.items() if n>=90]
print(s1)

'''
总结：
三元运算和所有的推导式（如果加了条件判断的话），
不管是什么推导式，我可以只筛选一个条件但不给不符合条件的元素定性，
但是三元运算必须写else，必须给不符合条件的元素定性
'''

'''
练习2：
给定气温列表 [35, 28, 40, 15, 38, 22, -5, 42]，要求：
先筛选出 ≥20 的气温
再对筛选后的气温用三元运算标记：≥38 标 "高温"，其余标 "正常"
最终输出标记列表
'''
te=[35, 28, 40, 15, 38, 22, -5, 42]
nte=[i for i in te if i>=20]
nnte=["高温" if i>=38 else "正常" for i in nte]
print(nnte)
