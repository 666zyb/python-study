'''
每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试 。
Python根据条件测试的值为True 还是False 来决定是否执行if 语句中的代码。如果
条件测试的值为True ，Python就执行紧跟在if 语句后面的代码；如果为False ，Python就忽略这些代码。
在if语句中，如果有多个条件都需要满足，则用and将各个条件连在一起，如果是多个条件中某一个或某几个条件满足即可，则用or连接
如果有多个分支的话，则可以使用if...elif...else...结构或者嵌套的if...else...结构，比如下面的分段函数求值例子
'''
# 下面是一个简单的if语句，用来身份验证
username = 'admin'
password = '123456'
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
### 身份验证成功!

'''
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
如果有多个分支则用更多的elif，一个if语句else最多只能有一个，但elif可以有多个
'''
x = 3
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(y)
### 4

'''
用if语句来处理列表，判断列表是否为空和判断列表中是否含有某个元素
'''
squres1 = [1, 2, 3, 4, 'apple']
if squres1 == []:
    print('该列表为空列表')
else:
    print('该列表不为空')
### 该列表不为空
if 'apple' in squres1:
    print('该列表中含有apple')
else:
    print('该列表中不含apple')
### 该列表中含有apple
