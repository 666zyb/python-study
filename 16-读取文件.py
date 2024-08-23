'''
从文件中读取数据
函数open()接受一个参数：要打开的文件的名称。
函数open()返回一个对象并存储到as后面的变量中
'''
# 以之前创建的moudele.py文件为例，读取里面的内容
with open('moudle.py') as mp:
    '''
    with称为上下文管理器，如果不调用with关键字，则在打开文件后需要调用close()函数去关闭文件，
    但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭，若未妥善地关闭文件可能会导致数据丢失或受损。
    如果在程序中过早地调用close()，会发现需要使用文件时它已关闭
    但是with关键字可以在不需要访问文件的时候自动关闭文件，不需要手动的去添加close()语句 
    '''
    conents = mp.read()  # 将moudle.py中的代码全部读取出来并打印
    print(conents)
### def moudle_1():
###     print('hello,Marry')
### def moudle_2():
###     print('Nice to meet you!')

'''
open()也可以读取电脑中的文件，需要写出要读取的文件的路径
'''
# 我在电脑文件里面新建了一个文本文档，在里面编辑了一个Hello World！
with open('D:\\pycharm  code\文件和异常.txt') as a1:
    # pycharm前面之所以有两个斜杠，是因为\p在代码里面属于固定的搭配，需要加一个转义字符\,代表\后面的\为普通的斜杠
    conents = a1.read()
    print(conents)
### Hello World!

'''
写入文件
调用open()时提供了两个实参。第一个实参也是要打开的文件的名称；第二个实参（'w' ）告诉Python，我们要以写入模式打开这个文件。
打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。
如果你省略了模式实参，Python将以默认的只读模式打开文件。
'''
with open('D:\\pycharm  code\文件和异常.txt', 'w') as a1:
    a1.write('I love you')
# 打开文件发现里面的Hello World！变成了I love you
