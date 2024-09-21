# MultiConvert.py
# 张三 + 学号 123456

def temp_convert(temp_str):
    """
    温度转换函数
    :param temp_str: 用户输入的带符号温度值
    :return: 转换后的温度值或者提示错误信息
    """
    if temp_str[-1] in ['F', 'f']:  # 如果输入的是华氏温度
        # 请补充代码：将华氏温度转换为摄氏温度的公式
        pass  # 替换为实际计算公式
    elif temp_str[-1] in ['C', 'c']:  # 如果输入的是摄氏温度
        # 请补充代码：将摄氏温度转换为华氏温度的公式
        pass  # 替换为实际计算公式
    else:
        return "输入格式错误"  # 错误提示

def length_convert(length_str):
    """
    长度转换函数
    :param length_str: 用户输入的带符号长度值
    :return: 转换后的长度值或者提示错误信息
    """
    if length_str[-1] in ['M', 'm']:  # 如果输入的是米
        # 请补充代码：将米转换为英尺的公式
        pass  # 替换为实际计算公式
    elif length_str[-1] in ['F', 'f']:  # 如果输入的是英尺
        # 请补充代码：将英尺转换为米的公式
        pass  # 替换为实际计算公式
    else:
        return "输入格式错误"  # 错误提示

def main():
    """
    主函数，控制整个转换流程
    """
    print("欢迎使用多功能转换器")
    while True:
        user_input = input("请输入带符号的温度或长度值（输入Q退出）：")
        if user_input.upper() == 'Q':  # 如果用户输入Q或q则退出程序
            print("程序结束")
            break
        elif user_input[-1].upper() in ['C', 'F']:  # 识别温度转换
            result = temp_convert(user_input)
            print(result)
        elif user_input[-1].upper() in ['M', 'F']:  # 识别长度转换
            result = length_convert(user_input)
            print(result)
        else:
            print("输入格式错误，请重新输入")

# 程序入口
if __name__ == "__main__":
    main()
