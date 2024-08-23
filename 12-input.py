'''
函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便使用。
'''
name = input('请输入你的名字:')  # 输入张三
print('Hello,' + name + '!')
### 请输入你的名字:张三
### Hello,张三!

'''
使用int() 来获取数值输入
注意：input()输入的都是字符串类型，所以一般情况下需要用int()方法进行转换，如果不需要转换，则无需用int()
type()方法可以用来检测数值类型
'''
age = input('How old are you?')  # 输入21，用type()输出age的类型，会发现为字符串类型
print(type(age))  ### <class 'str'>

# 一般情况下会直接用int()进行转换
age = int(input('How old are you?'))  # 输入21，用int()方法转换为整型
print(type(age))  ### <class 'int'>
