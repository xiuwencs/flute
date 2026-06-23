import numpy as np

# 计算信息熵的函数
def calculate_entropy(arr):
    unique_elements, counts = np.unique(arr, return_counts=True)
    probabilities = counts / len(arr)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def entropy(column):
    from collections import Counter
    from math import log2
    # 计算每个值的频率
    freq = Counter(column)
    total = len(column)
    entropy_value = 0
    for count in freq.values():
        p = count / total
        entropy_value -= p * log2(p)
    return entropy_value

def calculate(data,index):
    # 方法一
    entropy = []
    entropy1 = []
    for index_ in index :
        # 分成前后两部分
        part11 = []
        part22 = []
        entropy_ = []
        for i in range(len(data)):
            part1 = data[i][:index_]
            part2 = data[i][index_:]
            # 计算前12个元素的信息熵
            entropy_part1 = calculate_entropy(part1)
            part11.append(entropy_part1)
            # 计算后面部分的信息熵
            entropy_part2 = calculate_entropy(part2)
            part22.append(entropy_part2)
        entropy_.append(np.mean(part11))
        entropy_.append(np.mean(part22))
        entropy1.append(np.mean(part22) - np.mean(part11))
        entropy.append(entropy_)
#    print(entropy)
    return entropy1, entropy

def calculate1(data,index):
#    # 找到最长行的长度
#    max_length = max(len(row) for row in data)
#
#    # 创建一个新的二维数组，并用"00"填充到最长长度
#    padded_data = []
#    for row in data:
#        new_row = row + ["00"] * (max_length - len(row))
#        padded_data.append(new_row)
    # 找出最短行的长度
    min_length = min(len(row) for row in data)

    # 创建一个新的二维数组，根据最短长度截取每一行
    padded_data = []
    for row in data:
        truncated_row = row[:min_length]  # 截取当前行到最短长度
        padded_data.append(truncated_row)

    entropy = []
    entropy1 = []
    for index_ in index :
        part11 = []
        part22 = []
        entropy_ = []
        # 分成前后两部分
        for i in range(len(padded_data[0])):
            if i < index_:
                part1 = [row[i] for row in padded_data]
                # 计算前index_个元素的信息熵,[9,13],计算0,1，2,3,5,6,7,8列数据的信息熵平均值
                entropy_part1 = calculate_entropy(part1)
                part11.append(entropy_part1)
            else:
                part2 = [row[i] for row in padded_data]
                # 计算后index_个元素的信息熵
                entropy_part2 = calculate_entropy(part2)
                part22.append(entropy_part2)
        entropy_.append(np.mean(part11))
        entropy_.append(np.mean(part22))
        entropy.append(entropy_)
        entropy1.append(np.mean(part22) - np.mean(part11))
#    print(entropy1)
#    print(entropy)
    return entropy1, entropy

if __name__ == '__main__':

    calculate(data)

