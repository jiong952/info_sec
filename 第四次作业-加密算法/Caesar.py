# 加密
def encrypt(plaintext, key):
    ciphertext=""
    for c in plaintext:
        # 大写 65表示A
        if c.isupper():
            ciphertext += chr((ord(c) - 65 + key) % 26 + 65)
        # 小写 97表示a
        elif c.islower():
            ciphertext += chr((ord(c) - 97 + key) % 26 + 97)
        # 不是字母 无法加密
        else:
            ciphertext = ciphertext + c
    return ciphertext
# 解密
def decrypt(ciphtertext, key):
    plaintext=""
    for c in ciphtertext:
        if c.isupper():
            plaintext += chr((ord(c) - 65 - key) % 26 + 65)
        elif c.islower():
            plaintext += chr((ord(c) - 97 - key) % 26 + 97)
        else:
            plaintext = plaintext + c
    return plaintext
# 主函数
if __name__ == '__main__':
    option = input("请选择0（解密）或1（加密）: ")
    if option == '1':
        M = input("请输入明文：")
        K = int(input("请输入密钥："))
        print("密文为：", encrypt(M, K))
    elif option == '0':
        C = input("请输入密文：")
        K = int(input("请输入密钥："))
        print("明文为：", decrypt(C, K))
    else:
        print('请按照规则进行输入！')