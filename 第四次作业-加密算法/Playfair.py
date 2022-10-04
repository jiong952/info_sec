# 字母矩阵J统一用I
# 字母表 26个大写字母
alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
# 密钥去出重复字母
def remove_duplication(key):
    key = key.upper()
    _key = ''
    for c in key:
        if c == 'J':
            c = 'I'
        if c in _key:
            continue
        else:
            _key += c
    return _key

# 根据密钥构建字母矩阵
def get_matrix(key):
    key = remove_duplication(key)
    key = key.replace(' ', '')
    for c in alphabet:  # 根据密钥获取新组合的字母表
        if c not in key:
            key += c
    matrix = [[0 for i in range(5)] for j in range(5)]
    for i in range(len(key)):
        matrix[i // 5][i % 5] = key[i]
    return matrix

# 获取字符在字母矩阵中的坐标
def get_index(c, key):
    for i in range(5):
        for j in range(5):
            if c == key[i][j]:
                return i, j

# 加密两字母
def get_ctext(ch1, ch2, matrix):
    index1 = get_index(ch1, matrix)
    index2 = get_index(ch2, matrix)
    row1, col1, row2, col2 = index1[0], index1[1], index2[0], index2[1]
    # 同一行 向右循环取下一个
    if row1 == row2:
        ch1 = matrix[row1][(col1 + 1) % 5]
        ch2 = matrix[row2][(col2 + 1) % 5]
    # 同一列 向下循环取下一个
    elif col1 == col2:
        ch1 = matrix[(row1 + 1) % 5][col1]
        ch2 = matrix[(row2 + 1) % 5][col2]
    # 不同行不同列 取对应行列
    else:
        ch1 = matrix[row1][col2]
        ch2 = matrix[row2][col1]
    text = ''
    text += ch1
    text += ch2
    return text

# 加密
def encrypt(plaintext, key):
    # 大写 去除空白字符 替换J为I
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J", "I")
    plaintext = list(plaintext)
    # 末尾加标志 判断是否是奇数个字母
    plaintext.append('#')
    plaintext.append('#')
    # 获取字母矩阵
    matrix = get_matrix(key)
    ciphertext = ''
    i = 0
    while plaintext[i] != '#':
        # 相同插入K
        if plaintext[i] == plaintext[i + 1]:
            plaintext.insert(i + 1, 'K')
        # 最后多出一个
        if plaintext[i + 1] == '#':
            plaintext[i + 1] = 'K'
        ciphertext += get_ctext(plaintext[i], plaintext[i + 1], matrix)
        i += 2
    return ciphertext

# 解密两字母
def get_ptext(ch1, ch2, matrix):
    index1 = get_index(ch1, matrix)
    index2 = get_index(ch2, matrix)
    row1, col1, row2, col2 = index1[0], index1[1], index2[0], index2[1]
    # 同一行 向左循环取下一个
    if row1 == row2:
        ch1 = matrix[row1][(col1 - 1) % 5]
        ch2 = matrix[row2][(col2 - 1) % 5]
    # 同一列 向上循环取下一个
    elif col1 == col2:
        ch1 = matrix[(row1 - 1) % 5][col1]
        ch2 = matrix[(row2 - 1) % 5][col2]
    # 不同行不同列 取对应行列
    else:
        ch1 = matrix[row1][col2]
        ch2 = matrix[row2][col1]
    text = ''
    text += ch1
    text += ch2
    return text

# 解密 注意 由于加密如果末尾不足两字母会加一个K 因此解密过程无法判断是否加了K，因此保留所有K
def decrypt(ciphertext, key):
    matrix = get_matrix(key)
    i = 0
    plaintext = ''
    while i < len(ciphertext):
        plaintext += get_ptext(ciphertext[i], ciphertext[i+1], matrix)
        i += 2
    _plaintext = ''
    _plaintext += plaintext[0]
    for i in range(1, len(plaintext)-1):
        if plaintext[i] != 'K':
            _plaintext += plaintext[i]
        elif plaintext[i] == 'K':
            if plaintext[i-1] != plaintext[i+1]:
                _plaintext += plaintext[i]
    _plaintext += plaintext[-1]
    _plaintext = _plaintext.lower()
    return _plaintext

# 主函数
if __name__ == '__main__':
    option = input("请选择0（解密）或1（加密）: ")
    if option == '1':
        M = input("请输入明文：")
        K = input("请输入密钥：")
        print("密文为：",encrypt(M, K))
    elif option == '0':
        C = input("请输入密文：")
        K = input("请输入密钥：")
        print("明文为：",decrypt(C, K))
    else:
        print('请按照规则进行输入！')
