import math
import random

# 判断n是素数
def isPrime(p):
    # 素数的判断
    if p <= 1:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True

# 求最大公约数
def gcd(p, g):
    if g!=0:
        return gcd(g, p % g)
    else:
        return p

# 返回p的一个生成元 无则返回-1
def get_generator(p):
    # 得到所有的原根
    a = 2
    while a < p:
        if gcd(p,a) != 1 :
            continue
        flag = 1
        while flag != p:
            if (a ** flag) % p == 1:
                break
            flag += 1
        if flag == (p - 1):
            return a
        a += 1
    return -1

def exp_mod(b,n,m):
    return (b ** n) % m


if __name__ == "__main__":

    # 让用户输入素数
    p = int(input('请输入一个素数：'))
    while isPrime(p) == False:
        print('不是素数，请请重新输入！！')
        p = int(input(print('请输入一个素数')))
    print(str(p) + '是素数')

    # 得到素数的一个生成元
    g = get_generator(p)
    print(str(p) + ' 的一个原根为：' + str(g))

    # 得到A的私钥
    XA = random.randint(0, p - 1)
    print('A随机生成的私钥为：%d' % XA)

    # 得到B的私钥
    XB = random.randint(0, p - 1)
    print('B随机生成的私钥为：%d' % XB)

    # 得待A的计算数
    YA = exp_mod(g,XA,p)
    print('A的计算数为：%d' % YA)

    # 得到B的计算数
    YB = exp_mod(g, XB, p)
    print('B的计算数为：%d' % YB)

    # 交换后A的密钥
    key_A = exp_mod(YB,XA,p)
    print('A的生成密钥为：%d' % key_A)

    # 交换后B的密钥
    key_B = exp_mod(YA, XB, p)
    print('B的生成密钥为：%d' % key_B)

    print('A和B的密钥是否相等：',key_A == key_B)
