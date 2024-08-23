'''
使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类Dog ——它表示的不是特定的小狗，而是任何小狗。对于大多数宠物狗，
它们都有名字和年龄；大多数小狗还会蹲下和打滚。由于大多数小狗都具备上述两项信息（名字和年龄）和两种行为（蹲下和打滚），
Dog类将包含它们。这个类让Python知道如何创建表示小狗的对象。编写这个类后，将使用它来创建表示特定小狗的实例。
面向对象三大要素：继承，封装，多态
'''


class Dog(object):
    def __init__(self, name, age):
        '''
        每当你根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，
        这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
        方法__init__()定义成了包含三个形参：self 、name和age。
        在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面，在创建Dog类实例的时候，会自动传入实参self
        '''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟命令小狗坐下'''
        print(f'{self.name} is now sitting')

    def roll(self):
        '''模拟小狗正在打滚'''
        print(self.name + 'is now rolling')


dog_1 = Dog('张三', 6)  # 创建了一个dog_1的实例对象
dog_1.sit()  # 调用类里面的方法
print('My dog name is ' + dog_1.name + ',it is ' + str(dog_1.age) + ' age')  # 访问类里面的name和age属性
### 张三 is now sitting
### My dog name is 张三,it is 6 age

'''
继承和多态
在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。
提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，
'''


# 在下面这个例子中，Student类继承了Person类里面的属性和方法
# 其中Person为父类，Student为子类
class Person(object):
    '''人'''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    '''学生'''

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        '''
        super() 函数用于调用父类（超类）的方法。当你在一个子类中重写了父类的方法，但你又想保留父类原始方法的行为时，
        super() 就非常有用。使用 super()可以确保父类的方法被正确调用
        '''
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


stu = Student('张三', 17, '高三')
stu.study('数学')
stu.watch_av()
### 高三的张三正在学习数学.
### 张三只能观看《熊出没》.

from abc import ABCMeta, abstractmethod

'''
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写
通过方法重写可以让父类的同一个行为在子类中拥有不同的实现版本，当调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态
'''


# 下面这个例子里面Dog，Cat重写了父类Pet中的make_voice方法，使其在不同的实例中有不同的表现
# 比如在Cat里面表现为汪汪，在Cat里面表现为喵...喵...
class Pet(object, metaclass=ABCMeta):
    '''
    将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
    可以通过abc模块的ABCMeta和abstractmethod来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
    '''

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass


class Dog(Pet):
    '''狗'''

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    '''猫'''

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
for pet in pets:
    pet.make_voice()
### 旺财: 汪汪汪...
### 凯蒂: 喵...喵...
### 大黄: 汪汪汪...

'''
导入类
和导入函数的方法几乎一样
'''
