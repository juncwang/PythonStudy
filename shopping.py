#__author: JuncWang
#date: 2018/5/23

#__author: JuncWang
#date: 2018/5/23

salary = int(input("请输入你的资金 :\t"))
commodity = [ 'iphone6s','macbook','coffee','pythonbook','bicyle']
price = [5800,9000,32,80,1500]

PurCom = []
PurPri = []
PurInt = []
PurNum = 0


while True:
    print("请选择你想购入的物品 :\t")

    for i in range(5):
        print("%s.\t%s\t%s" % (i+1,commodity[i],price[i]))

    num = input("请输入你想购买商品的序号 :\t")

    if num == "quit":
        print("你所购买的物品有 :")
        for j in range(PurNum):
            print("%s.\t%s\t%s\t%s\t%s" % (j+1,PurCom[j],PurPri[j],PurInt[j],PurInt[j]*PurPri[j]))

        print("当前余额 :\t%s" %salary)
        break

    if num.isdigit():
        num = int(num)-1

        if 0 <= num < 5:

            if price[num] <= salary:
                salary -= price[num]
                print("已加入 %s 到你的购物车\t当前余额: %s" %(commodity[num],salary))

                if PurCom.count(commodity[num]) == 0:
                    PurCom.append(commodity[num])
                    PurPri.append(price[num])
                    PurInt.append(1)
                    PurNum += 1
                else:
                    PurInt[PurCom.index(commodity[num])] += 1

            else:
                print("余额不足\t%s" %(salary - price[num]))

        else:
            print("你输入的商品有误!")
    else:
        print("你输入的商品有误!")
