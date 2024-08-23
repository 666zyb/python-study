'''
异常是使用try-except代码块处理的。try-except 代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
使用了try-except 代码块时，即便出现异常，程序也将继续运行
try-except代码块中间是用来写可能会发生错误的代码，在except后面写入代码发生错误后要执行的操作
'''
a=int(input())
print(a)
print(f'用户输入的是：{a}')
#在上面的这三行代码，如果运行后用户输入的是不能转化为int()类型的，则程序会报错，那么后面的代码将不会执行
#但是如果用try-except代码块，则能够避免，比如下面的代码
try:
    a=int(input())
    print(a)
except:
    print('请重新输入，必须为数字')
    a=int(input())
    print(a)

'''
else代码块
else代码块是用来存放try里面的代码执行成功后要执行的操作
'''
#在这个代码中，如果输入的不能被转换为int类型，则执行except里面的代码，如果可以，则执行else里面的代码
try:
    a=int(input())
except:
    print('请重新输入，必须为数字')
    a=int(input())
else:
    print(a)
    print(f'用户输入的是：{a}')