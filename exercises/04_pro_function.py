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
record_goods = []

def price_calculate(goods_name,goods_price,goods_amount,key = False,discounts_paper = 0,discounts_point = 0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）计算订单的总金额。
    :param goods_name:
    :param goods_price:
    :param goods_amount:
    :param kwargs:key = True 录入完成,  discounts_paper,discounts_point(>=5000) 是否使用,输入数值
    :return: total price
    """
    record_goods.append([goods_name,goods_price,goods_amount])
    sum = 0
    if key:
        while len(record_goods) > 0:
            goods_name, goods_price, goods_amount = record_goods.pop(0)
            sum += goods_price * goods_amount
            print(f"goods name:{goods_name},goods amount:{goods_amount} total:{goods_price}")
        if sum >= 5000 and discounts_paper > 0 and discounts_point > 0:
            sum = sum - discounts_paper - discounts_point * 0.01
        elif sum >= 5000 and discounts_paper > 0:
            sum = sum - discounts_paper
        elif sum >= 5000 and discounts_point > 0:
            sum = sum - discounts_point * 0.01
        if sum >= 0:
            return sum
        else:return 0

price_calculate("apple",12,5)
price_calculate("orange",6,2.5)
price_calculate("banana",7,8)
result = price_calculate("pen",2000,5,key = True,discounts_paper = 520,discounts_point = 200)
print(result)

