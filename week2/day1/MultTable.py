#__author: JuncWang
#date: 2018/5/23

for i in range(1,10):
    for j in range(1,i+1):
        print( "%sx%s=%s" %(i,j,i*j),end="\t")
    print()