# 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
from turtledemo.penrose import sun


def triangle_area(height, width):
    """
    to calculate the area of a triangle
    :param height:
    :param width:
    :return: area
    """
    area = height * width * 1/2
    return area

# 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
def aeiou_num(s):
    """
    to calculate aeiou number
    :param s: string
    :return: number
    """
    return s.count('e') + s.count('a') + s.count('i') + s.count('u') + s.count('o')

# 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
def grade_statistics(l):
    """
    to statistics students grade
    :param l: students grade list[name,chinese grade,myth grade,english grade]
    :return: (the highest grade, the lowest grade, the average grade)(.1)
    """
    name, *score = l
    return max(score),min(score),round(sum(score)/len(score),1)
