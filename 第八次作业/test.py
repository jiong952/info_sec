from RSA import RSACipher

Alice = RSACipher('Alice')
Bob = RSACipher('Bob')
Nancy = RSACipher('Nancy')

messages = 'hello world!'
# 私钥签名
Alice.sign(messages)
# 测试使用收到的公钥进行解密
Bob.check(messages, Alice, Alice.crypto)
# 测试使用错误的公钥进行解密
Nancy.check(messages, Bob, Alice.crypto)