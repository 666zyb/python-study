"""
输入年份判断是不是闰年
"""
# year=int(input('请输入年份：'))
# #判断闰年：能被4整除且能被100整除  or  能被400整除
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f'{year}是闰年')
# else :
#     print(f'{year}是平年')

"""
英制单位英寸与公制单位厘米的互换
1英寸=2.54厘米
"""
# length=float(input('请输入长度：'))
# unit=input('请输入单位：')
# if unit=='英寸':
#     length1=2.54*length
#     print(f'{length:.2f}英寸={length1:.2f}厘米')
# else :
#     length1=length / 2.54
#     print(f'{length:.2f}厘米={length1:.2f}英寸')

"""
百分制成绩转换成等级制成绩
Grade>=90:A  
80<=Grade<90:B
70<=Grade<80:C
60<=Grade<70:D
Grade<60:E
"""
# Grade=int(input('请输入你的成绩：'))
# if Grade>=90:
#     print('A')
# elif 80<=Grade<90:
#     print('B')
# elif 70<=Grade<80:
#     print('C')
# elif 60<=Grade<70:
#     print('D')
# else :
#     print('E')

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
# import  math
# a=float(input('请输入边长：'))
# b=float(input('请输入边长：'))
# c=float(input('请输入边长：'))
# flag=a+b>c and a+c>b and b+c>a  #三角形任意两边之和大于第三边则能构成三角形
# if flag==True:
#     print('该三条边能够构成三角形')
#     perimeter=a+b+c
#     # 已知三边，用海伦公式计算面积：S=根号下p(p-a)(p-b)(p-c),p=(a+b+c)/2
#     p=perimeter/2
#     area=pow(p*(p-a)*(p-b)*(p-c),1/2)
#     print(f'三角形的周长为{perimeter:.2f},三角形的面积为{area:.2f}')
# else :
#     print('该三条边不能构成三角形')