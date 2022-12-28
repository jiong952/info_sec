import hashlib
import random

# 询问用户口令长度
pwd_length = int(input("请输入口令长度："))

# 生成随机字符串
random_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*', pwd_length))
print("生成的随机字符串为：")
print(random_str)

# 计算随机字符串的 Hash 值
random_str_hash = hashlib.sha256(random_str.encode()).hexdigest()
print("随机字符串的 Hash 值为：")
print(random_str_hash)

# 将 Hash 值作为口令
pwd = random_str_hash[:pwd_length]
print("生成的口令为：")
print(pwd)
