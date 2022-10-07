import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a1 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 22, 33], [44, 55, 66], [77, 88, 99]],
                   [[111, 222, 333], [444, 555, 666], [777, 888, 999]]])

    a1_dtype = str(a1.dtype)
    a1_shape = str(a1.shape)
    print(a1.dtype)  # 说明a1的dtype为int32
    print(a1.shape)  # 说明维度信息为(3,3,3)
    s = a1.tostring()
    print(type(s))  # 可知这里直接将数组转换成了字节串bytes

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
