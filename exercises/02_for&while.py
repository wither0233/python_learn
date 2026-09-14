#x以内的偶数相加

# num = int(input("Enter a number: "))
# sum = 0
# while num > 0:
#     if((num % 2) == 0):
#         sum = sum + num
#     num -= 1
# print(f"The sum is: {sum}")

#x以内的奇数相加

# num = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1,num+1):
#     if i % 2 != 0:
#         sum += i
# print(f"The sum is: {sum}")

#99乘法表

# for i in range (1,10):
#     for j in range (1,i + 1):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()

#猜数字游戏

# import random
# num = random.randint(1,325)
# input_num = int(input("Enter a number: "))
#
# while num != input_num:
#     if num > input_num:
#        input_num = int(input("too low"))
#     else:
#      input_num = int(input("too high"))
# else:
#     print("congratulation")

# 1000以内5的倍数累加

# num = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         num += i
# print(f"1000以内5的倍数和为{num}")

# st = input("Enter a string: ")
# num = 0
# for i in st:
#     if (i == "k" or i == "a"):
#         num += 1
# print(f"The number of a and k is {num}")