f = open('FileDictMenuData','r',encoding='utf-8')
data = ''
for line in f:
    data += line.strip()
f.close()
data = eval(data)

list_any = [data]
list_tmp = data

loopAll = True
isWrite = False

while loopAll:
    list_tmp = list_any[-1]
    for name in list_tmp:
        print(name)

    print("请输入想要查看的列表名[退出:q,上一级:b,添加:a,删除:d]".center(50,'='))
    inputName = input('===>>:\t')

    if inputName == 'q': loopAll = False
    elif inputName == 'b':
        if len(list_any) == 1: print("不能继续返回".center(50,'='))
        else:
            list_any.pop()
            list_tmp = list_any[-1]
    elif inputName in list_tmp:
        if len(list_tmp[inputName]) == 0:
            print("当前层级无资料，你可以输入:a 进行添加资料".center(50, '='))
        list_any.append(list_tmp[inputName])
    elif inputName == 'd':
        delName = input("请输入需要删除的省市县名称 :\t")
        if delName not in list_tmp:
            print("你输入的名称不存在".center(50, '='))
        else:
            list_tmp.pop(delName)
            isWrite = True
    elif inputName == 'a':
        addName = input("请输入需要添加的省市县名称 :\t")
        if addName not in list_tmp:
            list_tmp[addName] = eval('{}')
            isWrite = True
        else:
            print("你输入的名称已存在".center(50,'='))
    else:
        print("输入错误，请重新输入".center(50,'='))

    if isWrite:
        list_any[-1] = list_tmp
        f = open('FileDictMenuData', 'w', encoding='utf-8')
        f.write(str(list_any[0]))
        f.flush()
        f.close()
        isWrite = False
