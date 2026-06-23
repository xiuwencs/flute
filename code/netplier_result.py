import re

# 定义一个函数来去除元素中的'-'字符（如果存在的话）
def remove_dash(element):
    return element.replace('-', '')

def find_key(raw_key_index,file):
    with open(file, 'r') as file:
        # 读取第一行并去掉行尾的换行符
        first_line = file.readline().strip()
        # 再按空格分隔
        index_first_line = first_line.split()

    # print(first_line)# 01 010600 c7 16 3
    # print(index_first_line)# ['01', '010600', 'c7', '16', '3f', '63', '00', '00
    # print(index_first_line[raw_key_index[0]])# 04

    # 使用正则表达式去除所有非字母数字字符（空格、-等）
    # 检查是否为字符串类型
    if isinstance(first_line, str):
        # 使用正则表达式去除所有非字母数字字符（空格、-等）
        cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', first_line)
        # print(cleaned_line)# 01010600c7163f6300000000c0a86a8000000
        # 将字符串每两个字符分割并存入数组
        result = [cleaned_line[i:i + 2] for i in range(0, len(cleaned_line), 2)]
        # print(result)# ['01', '01', '06', '00', 'c7', '16', '3f', '63', '00',
    else:
        print("Error: first_line is not a string!")

    # 使用列表推导式来找到 'index_first_line[raw_key_index[0]]]' 的下标
    indices = [index for index, value in enumerate(result) if value == index_first_line[raw_key_index[0]]]
    # print(indices)

    subarray1 = index_first_line[raw_key_index[0]:]
    # print(subarray1)
    # 去除-
    concatenated_string1 = ''.join(remove_dash(element) for element in subarray1)
    # print(concatenated_string1)

    # 如果找到多个下标，则需要进一步判断
    if len(indices) > 1:
        # 通过寻找关键字后的字符串是否相等
        for index_ in indices:
            subarray2 = result[index_:]
            concatenated_string2 = ''.join(remove_dash(element) for element in subarray2)
            # print(concatenated_string2)
            if (concatenated_string1 == concatenated_string2):
                return index_ + 1
                break
        # 在这些下标中找到最接近 'index_first_line[raw_key_index[1]]]' 的下标
    else:
        return indices[0] + 1

if __name__ == '__main__':
    index = [39]
    file = "E:\cy\code\\test\\result\dhcp\\netplier_file\msa_fields_visual.txt"
    print("关键字在第",find_key(index,file),"字节")