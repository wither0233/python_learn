# a b c数值交换
# a, b, c = 1, 2, 3
# t = (a, b, c)
# b, c, a = t
# print(a, b, c)
from os import name

# 计算所有学生的总分，平均分，一并输出
# 统计各科分数最高分，最低分，平均分，一并输出
# 查找均分大于90的学生，并输出优秀


# 找出同时修了法语和艺术的学生
# 找出同时修了四门课的学生
# 找出选修了足球但没有选修篮球的学生
# 统计每一个学生选修的课程数量
# basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# print("同时修了法语和艺术的学生有：",french_set.intersection(art_set))
# print("同时修了四门课的学生有：",basketball_set.intersection(art_set).intersection(football_set).intersection(french_set))
# print("选修了足球但没有选修篮球的学生有：",football_set.difference(basketball_set))
# all_students = basketball_set | art_set | football_set | french_set
# while len(all_students) > 0:
#     i = all_students.pop()
#     num = 0
#     if i in basketball_set:num += 1
#     if i in art_set:num += 1
#     if i in football_set:num += 1
#     if i in french_set:num += 1
#     print(f"{i}选修了{num}门课")

# 完成购物车系统实现增删改查，使用字典结构存储商品数据，通过菜单栏与用户交互
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车。
print("########欢迎使用购物车系统########")
print("#         按1添加购物车         #")
print("#         按2修改购物车         #")
print("#         按3删除购物车         #")
print("#         按4查询购物车         #")
print("#         按5退出购物车         #")
shopping_car = {}
switch = int(input("choose your step:"))
while switch != 5:
    match switch:
        case 1:
            name = input("请输入商品名称：")
            if(name in shopping_car):
                switch = int(input(f"{name} is already in the shopping car, please choose another step:"))
                continue
            value = [float(input("请输入商品价格：")), int(input("请输入商品数量："))]
            shopping_car[name] = value
            switch = int(input("next step:"))
        case 2:
            name = input("请输入要修改的商品名称：")
            if name not in shopping_car:
                switch = int(input(f"{name} is not in the shopping car, please choose another step:"))
                continue
            shopping_car[name] = [float(input("商品价格：")), int(input("商品数量："))]
            switch = int(input("next step:"))
        case 3:
            name = input("请输入要删除的商品名称：")
            if name not in shopping_car:
                switch = int(input(f"{name} is not in the shopping car, please choose another step:"))
                continue
            del shopping_car[name]
            switch = int(input("next step:"))
        case 4:
            for item in shopping_car.keys():
                name = item
                print(f"商品名称：{name}，商品价格：{shopping_car[name][0]},商品数量：{shopping_car[name][1]}")
            switch = int(input("next step:"))
        case _:
            print("format error")
            break
