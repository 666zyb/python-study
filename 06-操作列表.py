'''
sort()方法可以对列表进行排序，并且为永久性的，不能还原
sorted()方法也可以对列表进行排序，但不改变原有的列表
sort()如果在括号里加入reverse=True,则为倒序排序
sort()和sorted()排序都是默认按照ASCLL码值的顺序进行排序,而且都不能对不同类型排序，比如列表中有整型，也有字符串
'''
list_2 = ['China', 'Chinese', 'people', '1', 'b']
print(sorted(list_2))  # 可以看到排序后再次输出列表，列表并没有改变
print(list_2)
### ['1', 'China', 'Chinese', 'b', 'people']
### ['China', 'Chinese', 'people', '1', 'b']
list_2.sort()  # 可以看到排序后输出列表不再是原来的列表，而是排序后的列表,所以为永久性的
print(list_2)
### ['1', 'China', 'Chinese', 'b', 'people']
list_2.sort(reverse=True)
print(list_2)
### ['people', 'b', 'Chinese', 'China', '1']
'''
reverse()方法可以使整个列表前后翻转，会永久性的修改列表，想要恢复则只需再次调用reverse()方法即可
len()可以计算列表的长度，即元素个数，也可以计算字符串的长度
'''
list_2.reverse()
print(list_2)
list_2.reverse()
print(list_2)
### ['1', 'China', 'Chinese', 'b', 'people']
### ['people', 'b', 'Chinese', 'China', '1']
print(len(list_2))
### 5
print(len(list_2[0]))
### 6
