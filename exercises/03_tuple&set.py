# a b c数值交换
# a, b, c = 1, 2, 3
# t = (a, b, c)
# b, c, a = t
# print(a, b, c)

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
