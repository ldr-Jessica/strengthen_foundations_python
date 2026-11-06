#字典的查找：.get(val),查找键值对后面的内容
d={"Jessica":"1","Tom":"2","sarah":"3","Tony":"4"}
name=input("请输入你想要知道的人")
val=d.get(name)
if val==None:
    print("这里没有这个人")
else:
    print(val)

#字典的循环遍历&嵌套
#1.for循环直接拿到key
for key in d:
    print(key,d[key])
#2.把所有的key保存在一个列表
#print(l(d.keys()))

