import random
import time

# 询问用户数字的位数
num_digits = int(input("请输入数字的位数："))

# 生成指定位数的随机数
random_number = random.randint(10**(num_digits-1), 10**num_digits-1)

# 询问用户输入次数
num_inputs = int(input("请输入记忆的次数："))
interval = int(input("请输入数字显示的时间："))

# 统计正确次数
num_correct = 0

# 多次询问用户输入记忆的数字
for i in range(num_inputs):
    random_number = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
    # 显示随机数
    print("记住下面的数字：")
    print(random_number)

    # 等待 5 秒钟，让用户记忆数字
    time.sleep(interval)

    # 清屏
    print("\033[2J")

    # 询问用户输入记忆的数字
    user_input = int(input("输入你记忆的数字："))

    # 检查用户输入是否与随机数匹配
    if user_input == random_number:
        print("正确！")
        num_correct += 1
    else:
        print("错误。正确的数字是：")
        print(random_number)

# 输出正确率
print("你一共记忆了 {} 次，正确 {} 次，正确率为 {}%。".format(num_inputs,num_correct,num_correct/num_inputs *100))
