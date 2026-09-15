# 10个数字排序，输出最大，最小，平均值
# import random
# s = []
# print("随机生成十个数字：")
# for i in range(10):
#     s.append(random.randint(1, 25))
# print(s)
# s.sort()
# print(s)
# print(f"最大值为{s[9]},最小值为{s[0]},平均值为{sum(s) / 10}")

# 合并列表元素并去重
# s1 = [1,2,3,4,5,6]
# s2 = [3,4,7,8,6,10]
# temp = []
# s = s1 + s2
# print(s)

# for i in range(len(s)):
#     for j in range(i + 1,len(s)):
#         if s[i] == s[j]:
#             temp.append(s[i])
# for item in temp:
#     # print(item,end=" ")
#     s.remove(item)
# print(s)

# 1-20的平方列表
# num = []
# for i in range(1,21):
#     num.append(i*i)
# print(num)

# 验证邮箱格式是否正确 包含一个@与至少一个.
# s = input("Enter your email: ")
# if s.count("@") == 1 and s.count(".") >= 1:
#     print("Email address is right")
# else:
#     print("Email address is wrong")

# 判断字符串是否回文
# s = input("请输入字符串：")
# s1 = s[::-1]
# if s==s1:
#     print(f"{s}是回文字符串")
# else:
#     print(f"{s}不是回文字符串")

# 输入十个字符串反转后大写，然后保存在列表中之后遍历列表输出
# print("请输入十个字符串：")
# l = []
# for i in range(1,11):
#     s = input(f"请输入第{i}个字符串：")
#     s1 = s[::-1]
#     l.append(s1.upper())
# print(l)