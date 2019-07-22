import re
def name_qq():
    """
    验证输入用户名和QQ号是否有效并给出对应的提示信息

    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
    """
    is_name = False
    is_qq = False

    while not is_name and not is_qq:
        name = input('请输入用户名')
        is_name = re.match(r'^[0-9a-zA-Z_]{6,20}$', name)

        if not is_name:
            print('请输入正确的用户名')

        qq = input('请输入qq号')
        is_qq = re.match(r'^[1-9]\d{4,11}$', qq)
        if not is_qq:
            print('请输入正确的qq号')

        if is_name and is_qq:
            print('输入信息有效！')

 
def phone():
    """ phone = input('请输入手机号')
    is_phone = re.match(r'^13\d{9}|14[47]{8}|15[0-35-9]{8}|17[678]{8}|18\d{9}$', phone)
    # 13[0-9] | 14[47] | 15[012356789]|17[6,7,8]|18[0-9]
    if not is_phone:
        print('请输入正确的手机号')
    else:
        print('手机号正确') """

    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    print(sentence)
    # 查找所有匹配并保存到一个列表中
    phone_list = re.findall(pattern, sentence)
    print(phone_list)
    print('----------华丽的分割线------------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    temps = re.finditer(pattern, sentence)
    for temp in temps:
        print(temp.group())
    print('----------华丽的分割线------------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def main():
    # name_qq()
    phone()

if __name__ == "__main__":
    main()