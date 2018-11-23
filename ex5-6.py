def recur_fibo(num):
    if num <= 1:
        return 1
    else:
        return recur_fibo(num - 1) + recur_fibo(num - 2)
you_need = int(input("你需要生成几项: "))
print("斐波那契函数")

for i in range(10):
    print(recur_fibo(i),end=" ")
