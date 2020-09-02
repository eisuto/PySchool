import random

level = int(input("请选择您的游戏等级\n0~50\t=> 1\n50~100\t=> 2\n100~150\t=> 3\n")) - 1
rSum = random.randint(level * 50, level * 50 + 50+1)
while True:
    iSum = int(input("请输入一个%d~%d之间的整数：" % (level * 50, level * 50 + 50)))
    if iSum > rSum:
        print("有点大了哦，再试试吧")
    elif iSum < rSum:
        print("有点小了哦，再试试吧")
    else:
        break
print("恭喜你猜对啦！")

