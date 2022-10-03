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