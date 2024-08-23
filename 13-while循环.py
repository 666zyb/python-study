'''
for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条件不满足为止。
'''
# 一个简单的while循环，打印1到5数字
count = 1
while count <= 5:
    print(count, end=' ')
    count += 1
### 1 2 3 4 5

# 可使用while 循环让程序在用户愿意时不断地运行,在其中定义了一个退出值，只要用户输入的不是这个值，程序就接着运行
while input() != '0':  # 注意：这里必须要和’0‘比较，而不是0，因为input()输入的是字符串’0‘，不是数字0，或者可以写成int(input())!=0
    print('继续玩')
print('退出循环')  # 当输入0的时候，while循环条件不成立，退出循环
### 1
### 继续玩
### 0
### 退出循环

'''
break语句：要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。
          break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
'''
while True:  # True表示条件成立，可以一直循环
    count = int(input('请输入一个数字：'))
    if count == 1:  # 当输入的数字不是1的时候，会执行else里面的语句，如果输入1，则执行break，直接跳出循环，执行下一步操作
        break
    else:
        print('你输入的数字是：', count)
print('跳出循环')
### 请输入一个数字：2
### 你输入的数字是： 2
### 请输入一个数字：3
### 你输入的数字是： 3
### 请输入一个数字：1
### 跳出循环

'''
continue语句：要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句，
             它不像break 语句那样不再执行余下的代码并退出整个循环。
也就是说如果执行continue语句，则continue后面的代码将直接跳过，然后执行下一次的循环
'''
# 例如下面这个代码：判断1到10中为偶数的数字并打印偶数的数字
# 首先将current_number设置成了0，由于它小于10，Python进入while循环。进入循环后，我们以步长1的方式往上数，因此current_number为1。
# 接下来，if语句检查current_number与2的求模运算结果。如果结果为1（意味着current_number不能被2整除），就执行continue 语句，
# 让Python忽略余下的代码，并返回到循环的开头。如果当前的数字能被2整除，就执行循环中余下的代码，Python将这个数字打印出来：
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue
    print(current_number)
### 2
### 4
### 6
### 8
### 10

'''
一个简单的调查程序代码的例子
其中的循环每次执行时都提示输入被调查者的名字和回答。我们将收集的数据存储在一个字典中，以
便将回答同被调查者关联起来：
'''
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # 将答卷存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
### What is your name? 张三
### Which mountain would you like to climb someday? yes
### Would you like to let another person respond? (yes/ no) yes

### What is your name? 李四
### Which mountain would you like to climb someday? no
### Would you like to let another person respond? (yes/ no) no

### --- Poll Results ---
### 张三 would like to climb yes.
### 李四 would like to climb no.
