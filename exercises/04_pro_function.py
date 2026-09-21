# # 计算数字的阶乘
# def factorial(num):
#     if num == 1:return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(5))

# ● 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）计算订单的总金额。
# 具体规则如下：
# • 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# • 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。

def price_calculate(*args:tuple[str,float,int],discounts_paper = 0,discounts_point = 0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）计算订单的总金额。
    :param args:商品信息:name,price,amount
    :param discounts_paper,discounts_point(>=5000) 如果能使用,输入数值
    :return: total price
    """
    total = 0
    for good_name,good_price,good_amount in args:
        total += good_price * good_amount
    if total >= 5000:
        total =total - discounts_point * 0.01 - discounts_paper
    if total >= 0:
        return total
    else:return 0

if __name__ == '__main__':
    goods = (("apple",12,5),("orange",6,2.5),("banana",7,8),("pen",2000,5))
    result = price_calculate(*goods,discounts_point = 5,discounts_paper=500)
    print(result)


