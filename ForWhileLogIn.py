#__author: JuncWang
#date: 2018/5/23

_user = "juncwang"
_pass = "Wang"

# num = 1
# while True:
#     username = input("请输入用户名\t: ")
#     password = input("请输入密码\t: ")
#
#     if _user == username and _pass == password:
#         print("登录成功")
#         break
#     else:
#         print("用户名或密码错误")
#         if num < 3:
#             num += 1
#             print("请重新输入")
#         else:
#             print("账户锁定")
#             break
#
# exit()

for i in range(3):
    username = input("请输入用户名\t: ")
    password = input("请输入密码\t: ")

    if _user == username and _pass == password:
        print("登录成功")
        break

    print("用户名密码错误，请重新输入")
else:
    print("用户被锁定，程序终止")

exit();