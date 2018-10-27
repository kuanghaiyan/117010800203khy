s=5
tem=0
while True:
    x=eval(input("请输入0~9之间的整数"))
    tem +=1
    if(x>s):
        print("遗憾,太大了")
    elif(x==s):
        print("预测了{}次,你猜中了".format(tem))
        break
    else:
        print("遗憾,太小了")

