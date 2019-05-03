"""
    作者：赵钦超
    功能：五角星的绘制
    版本：1.0
    时间：2019/04/03
"""

import turtle

def main():
    """
    主函数
    """
    #例子：绘制正方形
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.exitonclick()

    #绘制五角星

    # #绘制第一条边
    # turtle.forward(200)
    # turtle.right(144)
    #
    # #绘制第二条边
    # turtle.forward(200)
    # turtle.right(144)
    #
    # #绘制第三条边
    # turtle.forward(200)
    # turtle.right(144)
    #
    # #绘制第四条边
    # turtle.forward(200)
    # turtle.right(144)
    #
    # #绘制第五条边
    # turtle.forward(200)
    # turtle.right(144)
    #
    # #鼠标点击退出，否则图形绘制完毕后自动退出了！
    # turtle.exitonclick()

    #以上，程序重复性输入太多，改写成while循环格式
    count  = 1
    while count <= 5:
        turtle.forward(250)
        turtle.right(144)

        #配置计数器，累加次数，用于判断 count <=5
        count = count + 1

    turtle.exitonclick()

if __name__ == '__main__':
    main()