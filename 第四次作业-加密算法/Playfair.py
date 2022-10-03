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
# 主函数
if __name__ == '__main__':
    key = input()
    get_matrix(key)
