def temp_convert(temp_str):
    """
    温度转换函数
    :param temp_str: 用户输入的带符号温度值
    :return: 转换后的温度值或者提示错误信息
    """
    try:
        value = float(temp_str[:-1])  # 提取数值部分
    except ValueError:
        return "输入格式错误"

    if temp_str[-1] in ['F', 'f']:  # 如果输入的是华氏温度
        # 将华氏温度转换为摄氏温度的公式
        celsius = (value - 32) * 5 / 9
        return f"{value}华氏度 = {celsius:.2f}摄氏度"
    elif temp_str[-1] in ['C', 'c']:  # 如果输入的是摄氏温度
        # 将摄氏温度转换为华氏温度的公式
        fahrenheit = value * 9 / 5 + 32
        return f"{value}摄氏度 = {fahrenheit:.2f}华氏度"
    else:
        return "输入格式错误"  # 错误提示

def length_convert(length_str):
    """
    长度转换函数
    :param length_str: 用户输入的带符号长度值
    :return: 转换后的长度值或者提示错误信息
    """
    try:
        value = float(length_str[:-1])  # 提取数值部分
    except ValueError:
        return "输入格式错误"

    if length_str[-1] in ['M', 'm']:  # 如果输入的是米
        # 将米转换为英尺的公式
        feet = value * 3.28084
        return f"{value}米 = {feet:.2f}英尺"
    elif length_str[-1] in ['F', 'f']:  # 如果输入的是英尺
        # 将英尺转换为米的公式
        meters = value / 3.28084
        return f"{value}英尺 = {meters:.2f}米"
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
