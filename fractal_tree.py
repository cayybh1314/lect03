"""
    作者：赵钦超
    功能：利用迭代绘制分形树
    版本：1.0
    时间：2019/04/08
"""

import turtle

def draw_branch(branch_length):
    """
        绘制分形树
    """
    if branch_length > 5:
    #第一步先绘制右侧树枝
        turtle.forward(branch_length)
        #print('向前 ', branch_length)
        turtle.right(20)
        #print('右转 20')
        draw_branch(branch_length - 13)


        #第二步，绘制左侧树枝
        turtle.left(40)
        #print('左转 40')
        draw_branch(branch_length - 13)


        # 返回之前的树枝
        turtle.right(20)
        #print('右转 20')
        turtle.backward(branch_length)
        #print('向后 ', branch_length)


def main():
    """
    主函数
    """
    turtle.left(90)
    draw_branch(40)
    turtle.exitonclick()

if __name__ == '__main__':
    main()