# python 异或加密算法, 使用^来计算明文与密文的解译
import random

# 加密
def encrypt(plaintext, key):
    random.seed(key)
    ciphertext = ''
    for c in plaintext:
        ciphertext += str(ord(c) ^ random.randint(0, 255)) + ','
    ciphertext = ciphertext.strip(',')
    return ciphertext

# 解密
def decrypt(ciphtertext, key):
    random.seed(key)
    ciphtertext = ciphtertext.split(',')
    plaintext = ''
    for c in ciphtertext:
        c = int(c)
        plaintext += chr(c ^ random.randint(0, 255))
    return plaintext

# 主函数
if __name__ == '__main__':
    input_str = input('请选择0（解密）或1（加密）: ')
    if input_str == '1':
        M = input("请输入明文：")
        K = int(input("请输入密钥："))
        print("密文为：", encrypt(M, K))
    elif input_str == '0':
        C = input("请输入密文：")
        K = int(input("请输入密钥："))
        print("明文为：", decrypt(C, K))
    else:
        print('请按照规则进行输入！')