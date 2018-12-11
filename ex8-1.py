#e15.1MatchAnalysis.py
from random import random
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")
def getInputs():
    a=eval (input("请输入选手A的能力值（0-1）："))
    b=eval (input("请输入选手B的能力值（0-1）："))
    n=eval (input("模拟比赛的场次:"))
    return a, b, n
def simNGames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA, scoreB=simOneGame(probA,probB)
        if scoreA>scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB
def gameOver(a,b):
    if a==20 and b<20:
        return True
    elif a<21 and b==21:
        return True
    elif 21<a<30 and 21<b<30 and abs(a-b) ==2:
        return False
def simOneGame(probA, probB):
    scoreA,scoreB = 0, 0
    serving = 0
    t = 0
    while not gameOver(scoreA,scoreB):
        if serving == 0:
            if random() < probA:
                scoreA += 1
            else:
                serving=0
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving=0
    return scoreA, scoreB
def printSummary(winsA, winsB):
    n=winsA+winsB
    print("竞技分析开始,共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛,占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛,占比{:0.1%}".format(winsB,winsB/n))
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA,winsB)
main()

