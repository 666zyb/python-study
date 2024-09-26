# turtle库介绍
turtle库 是 Python 的一个标准库，它提供了一个简单而强大的图形绘制模块，特别适合于初学者学习编程和理解编程概念。使用 turtle，可以通过控制一个小海龟（画笔）在屏幕上移动来绘制各种图形和图案。

### 主要特性和功能
##### 1.图形窗口：turtle 提供了一个名为“屏幕”的图形窗口，用于显示绘制的图形。
##### 2.海龟（Turtle）：海龟是绘图的实体，它可以在屏幕上移动并留下轨迹。
##### 3.绘图命令：turtle 提供了一系列命令来控制海龟的移动和绘图行为，如前进、后退、左转、右转、抬笔、落笔等。
##### 4.画笔控制：可以设置画笔的颜色、大小、样式等属性。
##### 5.颜色和填充：可以设置图形的颜色和填充样式。
##### 6.事件处理：可以响应用户的操作，如鼠标点击、键盘输入等。
##### 7.动画：可以通过连续移动海龟来创建动画效果。
##### 8.保存图形：可以将绘制的图形保存为图片文件。
##### 9.自定义形状：可以定义和使用自定义的海龟形状。
##### 10.多海龟绘图：可以在屏幕上创建多个海龟对象，同时进行绘图。

## turtle库一些基本命令
```python
forward(distance) 或 fd(distance)：向前移动指定的距离。
backward(distance) 或 bk(distance)：向后移动指定的距离。
right(angle) 或 rt(angle)：向右转动指定的角度。
left(angle) 或 lt(angle)：向左转动指定的角度。
circle(radius) 或 cir(radius)：画一个指定半径的圆。
penup() 或 pu()：抬起笔，移动时不绘图。
pendown() 或 pd()：放下笔，移动时绘图。
color(color)：设置画笔的颜色。
fillcolor(color)：设置填充颜色。
begin_fill()：开始填充图形。
end_fill()：结束填充图形。
```
### 简单例子
#### 用turtle库绘制一个正方形和五角星
```python
import turtle
turtle.setup(500,500) # 设置窗体大小为（300，500）
turtle.begin_fill()  # 填充颜色的起始
turtle.color("blue")  # 设置画笔颜色
turtle.circle(50,extent=None,steps=4)
turtle.end_fill()  # 填充颜色的结束，填充起始和结尾中间代码绘制的图
turtle.width(width=10)  # 设置画笔宽度
turtle.penup()  # 抬笔
turtle.goto(0,0)
turtle.pendown()  # 落笔
turtle.begin_fill()
turtle.fillcolor("red")
turtle.left(50)
for _ in range(6):  # 绘制一个五角星
    turtle.right(108)
    turtle.forward(50)
    turtle.left(36)
    turtle.fd(50)
turtle.end_fill()
turtle.done()
```

#### 用turtle库绘制一个奥运五环
```python
import turtle
turtle.setup(500,500) # 设置窗体大小为（300，500）
def wuhuan():
    """绘制一个奥运五环"""
    turtle.width(10)
    turtle.right(90)
    turtle.color("blue")
    turtle.circle(50)
    turtle.color("red")
    turtle.circle(-50,extent=540)
    turtle.color("yellow")
    turtle.circle(50)
    turtle.right(90)
    turtle.color("green")
    turtle.circle(-50,extent=450)
    turtle.color("black")
    turtle.circle(50)
wuhuan()
turtle.done()
```
