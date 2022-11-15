from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
from Crypto.Hash import SHA

class RSACipher():
    '''
    RSA加密、解密、签名、验签工具类
    备注：# RSA的加密机制有两种方案一个是RSAES-OAEP，另一个RSAES-PKCS1-v1_5
        # 对同样的数据，用同样的key进行RSA加密， 每次的输出都会不一样；但是这些加密的结果都能正确的解密
    '''

    def read_xml(self,xmlfile):
        '''
        读取待加密明文方法
        '''
        with open(xmlfile, 'r', encoding="utf-8") as file:
            # 用open()将XML文件中的内容读取为字符串
            xmlstr = file.read()
            print(xmlstr)
        return xmlstr

    def encrypt_file(self,encrypt_file):
        '''
        保存加密后密文方法
        '''
        with open(encrypt_file, 'rb') as f:
            message = f.read()
        return message

    def Encrypt(self, message, publicKeyfile, out_file):
        '''
        加密方法
        :param message: 需要加密的明文
        :param publicKeyfile: 公钥文件
        :param out_file: 输出密文
        :return: 加密后的文本
        '''
        with open(publicKeyfile, 'r') as f:
            publicKey = f.read()
        pubKey = RSA.importKey(publicKey)
        cipher = Cipher_PKCS1_v1_5.new(pubKey)
        message = message.encode()

        # 分段加密，加密长度byte为8的倍数，最长不超出最大加密量（单位：byte）=秘钥长度/8-11
        length = len(message)
        default_length = 245
        offset = 0
        res = bytes()
        while length - offset > 0:
            if length - offset > default_length:
                _res = cipher.encrypt(message[offset:offset + default_length])
            else:
                _res = cipher.encrypt(message[offset:])
            offset += default_length
            res += _res
        encrypt_text=base64.b64encode(res)

        with open(out_file, 'wb') as f_w:
            f_w.write(base64.b64encode(res))
        return encrypt_text


    def Decrypt(self,message, privateKeyfile, out_file):
        '''
        解密方法
        :param message: 加密后的密文
        :param privateKey: 私钥文件
        :param out_file: 输出明文
        :return: 解密后的文本
        '''
        with open(privateKeyfile, 'r') as f:
            privateKey = f.read()
        rsaKey = RSA.importKey(privateKey)
        cipher = Cipher_PKCS1_v1_5.new(rsaKey)
        randomGenerator = Random.new().read
        message = base64.b64decode(message.decode())
        res = []
        for i in range(0, len(message), 256):
            res.append(cipher.decrypt((message[i:i + 256]),randomGenerator))
        plainText = bytes(b"".join(res)).decode()
        print(plainText)

        with open(out_file, 'w', encoding='utf-8') as f_w:
            f_w.write(plainText)
        return plainText

    def sign(self,message, private_sign_file):
        '''
        签名方法
        :param message: 需要签名的文本
        :param private_sign_file: 私钥文件
        :return: 签名信息
        '''
        with open(private_sign_file, 'r') as f:
            private_sign = f.read()

        message = message.encode()

        private_key = RSA.importKey(private_sign)
        # 根据sha算法处理签名内容
        hash_value = SHA.new(message)
        # 私钥进行签名
        signer = Sig_pk.new(private_key)
        signature = signer.sign(hash_value)

        result=base64.b64encode(signature).decode()

        return result # 将签名后的内容，转换为base64编码

    def verify(self,message,public_sign_file,signature):
        '''
        验签方法
        :param message: 需要验签的文本
        :param public_sign_file: 公钥文件
        :param signature: 签名信息
        :return: 验签结果
        '''
        with open(public_sign_file, 'r') as f:
            public_sign = f.read()
        signature = base64.b64decode(signature)
        # 将签名之前的内容进行hash处理
        public_key = RSA.importKey(public_sign)
        print(public_key)
        # 验证签名
        hash_value = SHA.new(message.encode())
        verifier = Sig_pk.new(public_key)
        return verifier.verify(hash_value, signature)


if __name__ == '__main__':
    #创建RSA加密实例
    rsacipher = RSACipher()
    xmlfile = r'tes.txt'
    message=rsacipher.read_xml(xmlfile) #待加密明文
    encryptFile = "encrypt.txt"  #加密后密文
    publicKeyfile="rsa.pub" #公钥加密

    # 加密
    encrypt_text = rsacipher.Encrypt(message,publicKeyfile,encryptFile)
    print('加密后:\n%s' % encrypt_text)

    # 签名
    private_sign_file="private.pem"  # 私钥签名
    signature = rsacipher.sign(message,private_sign_file)
    print('签名:\n%s' % signature)

    # 解密
    decryptFile ="deencrypt.txt" #输出解密内容
    privateFile = "rsa.key"  #私钥解密
    decrypt_text = rsacipher.Decrypt(encrypt_text,privateFile,decryptFile)
    print('解密后:\n%s' % decrypt_text)

    # 验签
    pubic_sign_file = "public.pem"  # 公钥验签
    result = rsacipher.verify(decrypt_text,pubic_sign_file,signature)
    print('验签:\n%s' % result)