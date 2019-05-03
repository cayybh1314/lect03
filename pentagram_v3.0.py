"""
    作者：赵钦超
    功能：五角星的绘制
    版本：1.0
    时间：2019/04/08
    新增功能：加入循环操作绘制重复不同大小的图形
    新增功能：使用迭代循环操作绘制重复不同大小的图形
"""

import turtle

def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # 配置计数器，累加次数，用于判断 count <=5
        count = count + 1


def draw_recursive_pentagram(size):
    """
    迭代绘制五角星
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # 配置计数器，累加次数，用于判断 count <=5
        count = count + 1

    #绘制完毕五角星，然后更新参数
    size = size + 10
    if size <= 150:
        draw_recursive_pentagram(size)

def main():
    """
    主函数
    """
    turtle.backward(30)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 100
    draw_recursive_pentagram(size)
    turtle.exitonclick()

if __name__ == '__main__':
    main()