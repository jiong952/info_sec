import hashlib
from pathlib import Path

dup = {}
# photo_path = 'E:\\picture'


def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


def build_dup_dict(dir_path, pattern='*.jpeg'):
    def save(file):
        hash = md5sum(file)
        if hash not in dup.keys():
            dup[hash] = [file]
        else:
            dup[hash].append(file)

    p = Path(dir_path)
    for item in p.glob('**/' + pattern):
        save(str(item))


def main():
    # 返回hash值为key长度大于1的文件
    def get_duplicate():
        return {k: v for k, v in dup.items() if len(v) > 1}

    photo_path = input("请输入查重路径：")
    build_dup_dict(photo_path)
    length = 0
    for hash, files in get_duplicate().items():
        length += len(files)
    print("已找到重复文件{}项".format(length))
    for hash, files in get_duplicate().items():
        print("========================================")
        for file in files:
            print("{}".format(file))


if __name__ == '__main__':
    main()