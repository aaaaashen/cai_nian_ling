import sys
time = 0
age = 18
while time<=3:
    a = int(input("请输入鼠鼠的年龄"))
    if age == a:
        print("老东西猜对了")
        break
    elif age < a:
        print("老东西猜大了")
        print("你还有{}次机会".format(2-time))
        time+=1
    elif age > a:
        print("老东西猜小了")
        print("你还有{}次机会".format(2-time))
        time+=1
    else:
        print("你要不看看你输入了甚么")
    if time==3:
        b = input(print("老东西还想接着猜吗(y or n)"))
        if b == "y":
            time = 0
        elif b == "n":
            print("老东西还是不够了解我捏")
            sys.exit()
        else:
            print("老东西好好回答")






