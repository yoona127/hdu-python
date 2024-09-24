def temperature_conversion(temp_input):
    # 检查输入是否以C或F结尾
    if temp_input.endswith('C'):
        # 摄氏度转换为华氏度
        celsius = float(temp_input[:-1])
        fahrenheit = celsius * 9/5 + 32
        return f"{fahrenheit:.2f}F"
    elif temp_input.endswith('F'):
        # 华氏度转换为摄氏度
        fahrenheit = float(temp_input[:-1])
        celsius = (fahrenheit - 32) * 5/9
        return f"{celsius:.2f}C"
    else:
        return "输入格式错误"

def length_conversion(length_input):
    # 检查输入是否以M或F结尾
    if length_input.endswith('M'):
        # 米转换为英尺
        meters = float(length_input[:-1])
        feet = meters / 0.3048
        return f"{feet:.2f}F"
    elif length_input.endswith('F'):
        # 英尺转换为米
        feet = float(length_input[:-1])
        meters = feet * 0.3048
        return f"{meters:.2f}M"
    else:
        return "输入格式错误"

def main():
    while True:
        user_input = input("请输入带有符号的温度值或长度值（例如100F或10M），输入'exit'退出：")
        
        if user_input.lower() == 'exit':
            break
        
        if user_input[-1] in ['C', 'F']:
            result = temperature_conversion(user_input)
        elif user_input[-1] in ['M', 'F']:
            result = length_conversion(user_input)
        else:
            result = "输入格式错误"
        
        print(f"输出：{result}")

if __name__ == "__main__":
    main()
