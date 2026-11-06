#猜数字——三元运算
num=int(input("请输入你要猜的整数："))
a=7
a="猜对了" if num==a else "猜错了"
print(a)

#判断奇偶数
num1=int(input("请输入你要判断的整数："))
b="奇数" if num1%2==1 else "偶数"
print(b)

#三元运算的嵌套
#猜数字
num2=int(input("请输入你要猜的整数："))
tn=9
a="猜对了" if num2==tn else "猜小了" if num2<tn else "猜大了"
print(a)