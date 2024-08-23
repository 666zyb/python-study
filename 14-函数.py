'''
要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该任务的函数，让Python运行
其中的代码。你将发现，通过使用函数，程序的编写、阅读、测试和修复都将更容易。
'''


# 定义一个函数，并进行传参
def hello(name):  # 简单的问候语
    print('Hello,' + name)


hello('张三')
### Hello,张三

'''
实参和形参：在函数hello()的定义中，变量name是一个形参——函数完成其工作所需的一项信息。
          在代码hello('张三') 中，值'张三'是一个实参 。
          实参是调用函数时传递给函数的信息。调用函数时，将要让函数使用的信息放在括号内。
          在hello('张三') 中，将实参'张三'传递给了函数hello()，这个值被存储在形参name中。
'''

'''
传递实参
位置实参和关键字实参，位置实参的顺序不能乱，关键字实参是传递给函数的名称—值对。
'''


# 位置实参
def animal(animal_kinds, pet_jiao):
    print(f'{animal_kinds}是这样叫的：{pet_jiao}')


animal('dog', '汪汪')  # 位置实参的顺序不能变，否则会发生错误或达不到预期效果


### dog是这样叫的：汪汪

# 关键字实参
def animal_1(animal_kinds, pet_jiao):
    print(f'{animal_kinds}是这样叫的：{pet_jiao}')


animal(pet_jiao='汪汪', animal_kinds='dog')  # 关键字实参顺序无关紧要


### dog是这样叫的：汪汪

# 默认值
def animal_2(animal_kinds, pet_jiao, count=1):
    print(f'{animal_kinds}是这样叫的：{pet_jiao}，我家有{count}只')


animal_2('dog', '汪汪')  # 如果在传参的时候没有给count传参，则会使用默认值1
animal_2('dog', '汪汪', 2)


### dog是这样叫的：汪汪，我家有1只
### dog是这样叫的：汪汪，我家有2只

# 一下这些方法都可以调用函数，使用哪种调用方式无关紧要，只要函数调用能生成自己希望的输出就行。使用对自己来说最容易理解的调用方式即可。
def animal_3(animal_kinds, pet_jiao, count=1):
    print(f'{animal_kinds}是这样叫的：{pet_jiao}，我家有{count}只')


animal_3('dog', '汪汪')
animal_3('dog', '汪汪', 2)
animal_3(pet_jiao='汪汪', animal_kinds='dog', count=2)
animal_3('dog', pet_jiao='汪汪')
### dog是这样叫的：汪汪，我家有1只
### dog是这样叫的：汪汪，我家有2只
### dog是这样叫的：汪汪，我家有2只
### dog是这样叫的：汪汪，我家有1只

'''
函数返回值
返回值可以是基本数据类型：如整数（int）、浮点数（float）、布尔值（bool）等，还有字符串，列表，字典，元组，集合，异常，
生成器，甚至是函数和其他自定义对象（包括类的实例）
'''


def sum_1(a, b):
    return a + b


print(sum_1(1, 2))  ### 3


# 返回字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


### {'first': 'jimi', 'last': 'hendrix'}

# 传递任意数量的实参,在形参的前面打一个星号，就能传递任意数量的实参
def animal_count(*animal):
    print(f'我家有许多动物，比如{animal}')


animal_count('dog', 'cat', 'sheep', '...')


### 我家有许多动物，比如('dog', 'cat', 'sheep', '...')

# 传递任意数量的关键字实参
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
# 在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少
def animal_jiao(**animal):
    print(animal)


animal_jiao(dog='汪汪', cat='喵喵')

'''
将函数存储在模块中
函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。
你还可以更进一步，将函数存储在被称为模块 的独立文件中，再将模块导入 到主程序中。
import 语句允许在当前运行的程序文件中使用模块中的代码。
'''
# 导入整个模块
import moudle

moudle.moudle_1()
moudle.moudle_2()
### hello,Marry
### Nice to meet you!

# 导入特定的函数
from moudle import moudle_1

moudle_1()
### hello,Marry

# 导入模块中的所有函数,和导入整个模块的区别就是导入模块在调用函数时要用模块名加函数名的方式调用
from moudle import *

moudle_1()
moudle_2()
### hello,Marry
### Nice to meet you!

# 使用as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名 ——函数的另一个名称，类似于外号。
from moudle import moudle_1 as m_1

m_1()
### hello,Marry

# 使用as给模块指定别名
# 给模块指定别名，通过给模块指定简短的别名，能够更轻松地调用模块中的函数
import moudle as m

m.moudle_1()
m.moudle_2()
### hello,Marry
### Nice to meet you!
