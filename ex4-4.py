from random import*
seed(0)
k=randint(0,100)
tem=0
while True:
    x=eval(input("请输入0~100之间的整数"))
    tem +=1
    if(x>k):
        print("遗憾,太大了")
    elif(x==k):
        print("预测了{}次,你猜中了".format(tem))
        break
    else:
        print("遗憾,太小了")

