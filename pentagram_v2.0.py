"""
    作者：赵钦超
    功能：五角星的绘制
    版本：1.0
    时间：2019/04/03
    新增功能：加入循环操作绘制重复不同大小的图形
"""

import turtle

def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # 配置计数器，累加次数，用于判断 count <=5
        count = count + 1

def main():
    """
    主函数
    """

    #以上，程序重复性输入太多，改写成while循环格式
    size = 100
    while size <= 200:
        #调用定义的函数
        draw_pentagram(size)
        #配置计数器，用于判断size <= 200
        #size = size + 30
        size += 10 #等价于上面
    turtle.exitonclick()

if __name__ == '__main__':
    main()