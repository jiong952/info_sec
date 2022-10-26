import random


def pow_mod(p, q, n):
    '''
    幂模运算，快速计算(p^q) mod (n)
    这里采用了蒙哥马利算法
    '''
    res = 1
    while q:
        if q & 1:
            res = (res * p) % n
        q >>= 1
        p = (p * p) % n
    return res


def gcd(a, b):
    '''
    欧几里得算法求最大公约数
    '''
    while a != 0:
        a, b = b % a, a
    return b


def mod_1(x, n):
    '''
    扩展欧几里得算法求模逆
    取模负1的算法:计算x2= x^-1 (mod n)的值
    '''
    x0 = x
    y0 = n
    x1 = 0
    y1 = 1
    d = 1
    y2 = 0
    while n != 0:
        q = x // n
        (x, n) = (n, x % n)
        (x1, d) = ((d - (q * x1)), x1)
        (y1, y2) = ((y2 - (q * y1)), y1)
    if d < 0:
        d += y0
    if y2 < 0:
        y2 += x0
    return d


def probin(w):
    '''
    随机产生一个伪素数，产生 w表示希望产生位数
    '''
    list = []
    list.append('1')  # 最高位定为1
    for i in range(w - 2):
        c = random.choice(['0', '1'])
        list.append(c)
    list.append('1')  # 最低位定为1
    # print(list)
    res = int(''.join(list), 2)
    return res


def prime_miller_rabin(a, n):  # 检测n是否为素数
    '''
    第一步，模100以内的素数，初步排除很显然的合数
    '''
    list = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
                 , 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)  # 100以内的素数，初步排除很显然的合数
    for y in list:
        if n % y == 0:
            return False

    '''
    第二步 用miller_rabin素数判定算法对n进行检测
    '''
    if pow_mod(a, n - 1, n) == 1:  # 如果a^(n-1)!= 1 mod n, 说明为合数
        d = n - 1  # d=2^q*m, 求q和m
        q = 0
        while not (d & 1):  # 末尾是0
            q = q + 1
            d >>= 1
        m = d
        for i in range(q):  # 0~q-1, 我们先找到的最小的a^u，再逐步扩大到a^((n-1)/2)
            u = m * (2 ** i)  # u = 2^i * m
            tmp = pow_mod(a, u, n)
            if tmp == 1 or tmp == n - 1:
                # 满足条件
                return True
        return False
    else:
        return False


def prime_test(n, k):
    while k > 0:
        a = random.randint(2, n - 1)
        if not prime_miller_rabin(a, n):
            return False
        k = k - 1
    return True


# 产生一个大素数(bit位)
def get_prime(bit):
    while True:
        prime_number = probin(512)
        for i in range(50):  # 伪素数附近50个奇数都没有真素数的话，重新再产生一个伪素数
            u = prime_test(prime_number, 5)
            if u:
                break
            else:
                prime_number = prime_number + 2 * (i)
        if u:
            return prime_number
        else:
            continue


if __name__ == '__main__':
    p = get_prime(512)  # 密钥p
    q = get_prime(512)  # 密钥q
    n = p * q  # 公钥n
    OrLa = (p - 1) * (q - 1)  # 欧拉函数

    while True:  # 取一个合适的e，这里的e要和OrLa互素才行 一般取65537
        e = 65537
        if gcd(e, OrLa) == 1:
            break
        else:
            e = e - 1

    d = mod_1(e, OrLa)

    print('私钥p,q,d分别为:')
    print('p: %d' % p)
    print('q: %d' % q)
    print('d: %d' % d)

    print('公钥n,e分别为:')
    print('n: %d' % n)
    print('e: %d' % e)

    M = int(input("请输入待加密的明文："))

    C = pow_mod(M, e, n)  # 加密
    print('加密完成，得到的密文：%d' % C)

    M = pow_mod(C, d, n)  # 解密
    print('解密完成，得到的明文为：%d' % M)





