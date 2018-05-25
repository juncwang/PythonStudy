#__author: JuncWang
#date: 2018/5/23

salary = int(input("请输入你的资金 :\t"))

product_list = [
    ('iphone6s',5800),
    ('macbook',9000),
    ('coffee',32),
    ('pythonbook',80),
    ('bicyle',1500)
]

buy_list = []

while True:
    print("请选择你想购入的物品 :\t")

    for i,v in enumerate(product_list,1):
        print("%s.---------------------\t%s\t%s" % (i,v[0],v[1]))

    num = input("请输入你想购买商品的序号[exit:q] :\t")

    if num == "q":
        if len(buy_list) != 0:
            print("你所购买的物品有 :")
            for j,l in enumerate(buy_list,1):
                print("%s.---------------------\t%s\t%s" % (j,l[0],l[1]))

        print("当前余额 :\t%s" %salary)
        break

    if num.isdigit():
        num = int(num)-1

        if 0 <= num < 5:
            p_item = product_list[num]
            if p_item[1] <= salary:
                salary -= p_item[1]
                print("已加入 %s 到你的购物车\t当前余额: %s" %(p_item[0],salary))
                buy_list.append((p_item[0],p_item[1]))

            else:
                print("余额不足\t%s" %(salary - p_item[1]))

        else:
            print("你输入的商品有误!")
    else:
        print("你输入的商品有误!")
