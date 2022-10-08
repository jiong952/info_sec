# 读取文本文件
from algorithm import Caesar


def read_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        contents = f.read()
    return contents.rstrip()
# 写入文本文件 覆盖写 用于加密
def write_file(file_path,content):
    with open(file_path,'w', encoding='utf-8') as f:
        f.write(content)
