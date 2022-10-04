import numpy as np

class Hill:
    def __init__(self, m: int, fillchar: str = "K", key: np.ndarray = None):
        self.m = m  # 秘钥的维度
        self.ckey = key  # 加密秘钥
        self.pkey = None  # 解密秘钥
        # {0: "a", ...} 字符字典 用于转为字符
        self.num2char = {i: chr(ord("A") + i) for i in range(26)}
        # {0: "a", ...} int字典 用于转为int
        self.char2num = dict(zip(self.num2char.values(), self.num2char.keys()))
        self.fillChar = self.char2num[fillchar]  # 填充字符

    def setM(self, m: int) -> None:
        """设置秘钥的维度"""
        assert m > 0, "请输入一个大于0的数"
        self.m = m

    def setKey(self, key: np.ndarray = None) -> None:
        if key is None:  # 生成直到行列式有逆元为止
            while key is None or Hill.modInv(np.linalg.det(key)) == -1:
                key = np.random.randint(0, 27, size=(self.m, self.m))
            print("自动生成加密密钥：\n", *key.flatten())
            print("复制：", key)
        else:
            assert Hill.modInv(np.linalg.det(key)) != -1, "此秘钥无逆元，请重新输入！"
        y = Hill.modInv(np.linalg.det(key)) # 行列式乘法逆元
        K_inv = np.linalg.inv(key) # K的逆矩阵
        K_det = np.linalg.det(key) # K的行列式
        K_star = np.around(K_inv * K_det % 26).astype(np.int64) # K的伴随矩阵
        self.pkey = y * K_star % 26 # 解密矩阵
        self.ckey = key

    def setPkey(self, key: np.ndarray = None) -> None:
        self.pkey = key

    @staticmethod
    def modInv(x: int):
        """
        求 x 逆元 y，需满足：(x×y) mod 26 = 1
        :param x:
        :returns: 存在返回逆元 y，否则返回 -1
        """
        y = 0
        while y < 26:
            y += 1
            if (x * y) % 26 == 1:
                return y
        return -1

    def _loopCrypt(self, text: np.ndarray, K: np.ndarray) -> np.ndarray:
        """
        滑动矩阵加密解密
        :param text: 长文
        :param K: 做乘积的方阵
        """
        ans = np.array([])
        for i in range(text.shape[0] // self.m):
            ans = np.mod(np.hstack((
                ans,
                np.dot(text[i * self.m:i * self.m + self.m], K)
            )), 26)
        return ans.astype(np.int64)

    def encrypt(self, plaintext: np.ndarray):
        # 明文长度和加密长度不符 不够整除，填充字符
        if plaintext.shape[0] % self.m:
            plaintext = np.hstack((
                plaintext,
                [self.fillChar] * (self.m - plaintext.shape[0] % self.m)
            ))
        # 循环加密
        return self._loopCrypt(plaintext, self.ckey)

    def decrypt(self, ciphertext: np.ndarray):
        # 循环解密 注意解密无法去除加密过程补充的字符
        return self._loopCrypt(ciphertext, self.pkey)

    def translate(self, s, to: str):
        # 输入text转为字符矩阵
        # 输入num转为数值矩阵
        if to == "text":
            return "".join([self.num2char[si] for si in s]).strip(" ")
        elif to == "num":
            # 删除空格
            s = s.replace(" ", "")
            return np.array([self.char2num[si] for si in s])

# 主函数
if __name__ == '__main__':
    option = input("请选择0（解密）或1（加密）: ")
    dim = int(input("请输入密钥的维度："))
    hill = Hill(m=dim)
    if option == '1':
        text = input("请输入明文：")
        text = text.upper()
        choice = input("是否手动输入密钥? （Y/N）")
        if choice == 'Y':
            K = input("请输入加密密钥（空格隔开）：")
            K = [int(n) for n in K.split()]
            K = np.array(K)
            K = K.reshape((dim, dim))
            hill.setKey(K)
        else:
            hill.setKey()
        print("解密秘钥是:\n", hill.pkey,)  # 打印解密秘钥
        print("解密秘钥(供复制)：", *hill.pkey.flatten(), "\n")  # 打印解密秘钥
        nums = hill.translate(text, "num")
        result = hill.encrypt(nums)
        print("密文为：", *result, "\n")
    elif option == '0':
        # 读入密文
        ciphertext = input("请输入密文（空格隔开）：")
        ciphertext = [int(n) for n in ciphertext.split()]
        ciphertext = np.array(ciphertext)
        # 读入解密密钥
        pkey = input("请输入解密密钥（空格隔开）：")
        pkey = [int(n) for n in pkey.split()]
        pkey = np.array(pkey)
        pkey = pkey.reshape((dim,dim))
        hill.setPkey(pkey)
        nums = hill.decrypt(ciphertext)
        res = hill.translate(nums, "text")
        print("解密后的明文是：\n", res, "\n")
    else:
        print('请按照规则进行输入！')