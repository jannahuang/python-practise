from random import random

'''
六爻算法实现
'''


# 随机选一组拿掉 1 颗棋子
def random_pick_1(a, b):
    dice = random()
    # 随机分组其中一组可能为 0
    if a == 0:
        b -= 1
        print("从右边中拿掉 1 颗棋子")
    elif b == 0:
        a -= 1
        print("从左边中拿掉 1 颗棋子")
    else:
        if 0 <= dice < 0.5:
            a -= 1
            print("从左边中拿掉 1 颗棋子")
        else:
            b -= 1
            print("从右边中拿掉 1 颗棋子")
    return a, b


# 计算余数，即该拿掉的棋子，返回剩余棋子数和拿掉棋子数
def subtract_remainder(r):
    # 当棋子余数为 0，不可能再拿
    if r == 0:
        r = 0
        c = 0
    else:
        c = r % 4
        if r % 4 == 0:
            r -= 4
            c = 4
        else:
            r -= r % 4
    return r, c


# 最初棋子总数
total = 49
# 用 for 循环重复三变
for i in range(3):
    print("第 {} 变".format(i+1))

    # 第一步：用 random 将棋子随机分成两组
    group_left = int(random() * total)
    group_right = total - group_left
    print("左右组分别有：", group_left, group_right)

    # 第二步：调用 random_pick_1 随机拿掉 1 颗棋子
    group_left, group_right = random_pick_1(group_left, group_right)
    print("拿掉 1 颗后左右组分别剩：", group_left, group_right)

    # 第三、四步：拿掉余数棋子
    group_left, left_remainder = subtract_remainder(group_left)
    group_right, right_remainder = subtract_remainder(group_right)
    print("拿掉余数后左右组分别剩：", group_left, group_right)

    # 第五步：已拿掉的棋子总数
    already_taken_out = 1 + left_remainder + right_remainder
    print("总共拿掉的棋子：", already_taken_out)

    # 剩余棋子总数，作为下一变的总数
    total -= already_taken_out
    print("剩余的棋子总数：", total, "\n")
