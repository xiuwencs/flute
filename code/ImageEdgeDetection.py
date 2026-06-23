import numpy as np
import matplotlib.pyplot as plt
# 转换为十进制进行灰度图处理
def hex_to_decimal(hex_data):
    # 将十六进制数据转换为十进制
    return [int(x, 16) for x in hex_data]

def data_to_image(data, shape):
    # 将一维数据转换为指定形状的二维数组
    data_array = np.array(data).reshape(shape)
    # 将数据映射到灰度值（0-255）
    data_normalized = (data_array - np.min(data_array)) / (np.max(data_array) - np.min(data_array))
    image = (data_normalized * 255).astype(np.uint8)
    return image

def concatenate_images(images, axis=0):
    # 按指定轴拼接图像
    return np.concatenate(images, axis=axis)

def preprocess(data_packets):
    # 找到最短的长度
    min_length = min(len(packet) for packet in data_packets)

    # 截取每个数据包到最短长度
    trimmed_packets = [packet[:min_length] for packet in data_packets]

    return min_length, trimmed_packets

def edge_detection(output_file,data_packets, Original_image):

    # 对数据包进行预处理，截取和填充
    min_length,trimmed_packets = preprocess(data_packets)

    # 将十六进制数据包转换为十进制
    decimal_packets = [hex_to_decimal(packet) for packet in trimmed_packets]

    # 转换数据包为图像
    # 将每个数据包转换为形状为 (1, min_length) 的二维数组
    shape = (1, min_length)

    images = [data_to_image(packet, shape) for packet in decimal_packets]

    # 拼接图像
    concatenated_image = concatenate_images(images, axis=0)
    # print(decimal_packets)
    # print("____________________________")
    decimal_packets = np.array(decimal_packets, dtype=np.uint8)

    # print(decimal_packets)
    # array_shape = decimal_packets.shape
    # print(f"数组的大小: {array_shape}")

    # 方法一 ：
    import cv2
    resized_image = cv2.resize(concatenated_image, (640, 480))
    cv2.imwrite(Original_image, resized_image)

    # 隐藏坐标轴
    # current_axes = plt.axes()
    # current_axes.xaxis.set_visible(False)
    # current_axes.yaxis.set_visible(False)
    # 显示拼接后的图像
    plt.imshow(concatenated_image, cmap='gray', aspect='auto')

    # 设置坐标轴范围和刻度
    # plt.xlim(0, decimal_packets.shape[1])  # 设置横坐标范围
    # plt.ylim(0, decimal_packets.shape[0])  # 设置纵坐标范围
    # plt.xticks(np.arange(0, decimal_packets.shape[1], decimal_packets.shape[1] // 10))  # 设置横坐标刻度间隔
    # plt.yticks(np.arange(0, decimal_packets.shape[0], decimal_packets.shape[0] // 10))  # 设置纵坐标刻度间隔
    plt.title(output_file + '_Original_image')

    # plt.show()
    return  decimal_packets



if __name__ == '__main__':
    from Import_hex import import_file
    # pcapng_file = 'E:\cy\code\code\dataset\gh0st.pcapng'
    # trans_file = 'E:\cy\code\code\dataset\gh0st.xlsx'
    # output_file = 'gh0st'

    # pcapng_file = 'E:\cy\code\code\dataset\dns.pcapng'
    # trans_file = 'E:\cy\code\code\dataset\dns.xlsx'
    # output_file = 'dns'

    # pcapng_file = 'E:\cy\code\code\dataset\dhcp.pcapng'
    # trans_file = 'E:\cy\code\code\dataset\dhcp.xlsx'
    # output_file = 'dhcp'

    # pcapng_file = 'E:\cy\code\code\dataset\modbus.pcapng'
    # trans_file = 'E:\cy\code\code\dataset\modbus.xlsx'
    # output_file = 'modbus'

    pcapng_file = 'E:\cy\code\code\dataset\\nbns.pcapng'
    trans_file = 'E:\cy\code\code\dataset\\nbns.xlsx'
    output_file = 'nbns'

    # pcapng_file = 'E:\cy\code\code\dataset\TLS.pcapng'
    # trans_file = 'E:\cy\code\code\dataset\TLS.xlsx'
    # output_file = 'TLS'

    # pcapng_file = 'E:\cy\code\code\dataset\smb.pcapng'
    # trans_file = 'E:\cy\code\code\dataset\smb.xlsx'
    # output_file = 'smb'


    import_data = import_file(pcapng_file, trans_file, output_file)
    current_data = []
    for i in range(len(import_data)): #1357,1358
        current_data.append(import_data[i])


    decimal_packets = edge_detection(output_file, current_data)
    print(decimal_packets)
    print(decimal_packets.shape[0])
    print(decimal_packets.shape[1])

