import rsa
import hashlib



class RSACipher:
    def __init__(self, name):
        self.name = name
        self.crypto = ''
        (self.pubkey, self.privkey) = rsa.newkeys(512)

    # 使用私钥进行加密
    def sign(self, str):
        md5_hash = hashlib.md5((str + self.name).encode()).hexdigest()
        self.crypto = self.rsaEncrypt(md5_hash, self.privkey)
        print('{}签名成功！'.format(self.name))
        return self.crypto
    # 使用公钥进行解密，对比hash值
    def check(self, str, user, crypto):
        if self.rsaDecrypt(hashlib.md5((str + user.name).encode()).hexdigest(), crypto, user.pubkey):
            print('{}验证签名成功！消息来自{}'.format(self.name, user.name))
        else:
            print('{}验证失败，消息被破坏...'.format(self.name))

    def rsaEncrypt(self, str, privk):
        content = str.encode('utf-8')
        crypto = rsa.sign(content, privk, 'MD5')
        return crypto

    def rsaDecrypt(self, mess, signa, pubk):
        try:
            rsa.verify(mess.encode(), signa, pubk)
        except rsa.VerificationError:
            result = False
        else:
            result = True
        return result
