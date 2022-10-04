## 加密算法

## 版本说明

新增Caesar加密算法

## 凯撒加密算法

**原理**

- 移位密码 将字母c用其后面的第k个字母进行替换
- 密钥k
- C = E(p) = (p + K) mod 26
- p = D(C) = (C - K) mod 26

适用：英文字母

**测试实例：**

![image-20221003233839320](C:\Users\Mono\Desktop\大三作业\信息安全概论\第四次作业-加密算法\img\image-20221003233839320.png)

![image-20221003233902436](C:\Users\Mono\Desktop\大三作业\信息安全概论\第四次作业-加密算法\img\image-20221003233902436.png)

## 异或加密算法

**原理**

- 数A经过密钥key两次异或运算可以恢复为A

- 利用python的`random.seed(key)` 随机种子

```python
def encrypt(plaintext, key):
    random.seed(key)
    ciphertext = ''
    for c in plaintext:
        ciphertext += str(ord(c) ^ random.randint(0, 255)) + ','
    ciphertext = ciphertext.strip(',')
    return ciphertext
```

**测试实例：**

![image-20221003234338192](C:\Users\Mono\Desktop\大三作业\信息安全概论\第四次作业-加密算法\img\image-20221003234338192.png)

![image-20221003234419946](C:\Users\Mono\Desktop\大三作业\信息安全概论\第四次作业-加密算法\img\image-20221003234419946.png)

## Playfair加密算法

**原理：**

- 根据输入的关键词密钥去重生成字母矩阵，采用多字母替换
- 字母矩阵的J统一使用I
- 针对同行、同列、不同行不同列采用不同的替换方式
- 默认填充字母K

**测试实例：**

加密：

![image-20221004132923556](C:\Users\Mono\Desktop\大三作业\信息安全概论\第四次作业-加密算法\img\image-20221004132923556.png)

解密：

注意：解密过程存在缺陷，最后一个字母无法判断是加密填充还是手动输入

![image-20221004133014667](C:\Users\Mono\Desktop\大三作业\信息安全概论\第四次作业-加密算法\img\image-20221004133014667.png)