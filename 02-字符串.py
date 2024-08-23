'''
将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名
title()方法可以将字符串中分隔开的每个单词首字母大写，并不是整个字符串的第一个字母
upper()方法可以将整个字符串字母转换为大写
lower()方法可以将整个字符串字母转换为小写
'''
name = 'Zhang Xiansheng'
print(name.upper())
### ZHANG XIANSHENG
print(name.lower())
### zhang xiansheng
print(name.title())
### Zhang Xiansheng


'''将信息存储在变量里面，并打印包含这个变量的消息'''
name = 'Zhang Xiansheng'
print(f'Are you {name}?')
### Are you Zhang Xiansheng?


'''
删除字符串中的空白
lstrip()方法可以删除字符串左边的空白
rstrip()方法可以删除字符串右边的空白
strip()方法可以删除字符串左右两边的空白
'''
name = '  Zhang Xiansheng  '
print(name.lstrip())
### Zhang Xiansheng
print(name.rstrip())
### Zhang Xiansheng
print(name.strip())
### Zhang Xiansheng
