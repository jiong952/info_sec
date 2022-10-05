import matplotlib.pyplot as plt
# 功能函数
def countchar(string):
    l = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    countList = []
    string = string.upper()
    for i in range(len(l)):
        countList.append(string.count(l[i]))
    return countList

# 绘制折线图
def paint(beforeStr,afterStr):
    x = [chr(ord("A") + i) for i in range(26)]
    beforeDir = zip(x,beforeStr)
    print("加密前：",dict(beforeDir))
    afterDir = zip(x,afterStr)
    print("加密后：", dict(afterDir))
    # 为正常显示中文字体，添加的代码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x, beforeStr,color='green',label='before')
    plt.plot(x, afterStr,label='after')
    plt.legend(loc='upper right')
    plt.xlabel('count')
    plt.ylabel('character')
    plt.title("加密前后字符对比图")
    plt.show()
if __name__ == "__main__":
    string1 = input()
    string2 = input()
    before = countchar(string1)
    after = countchar(string2)
    paint(before,after)