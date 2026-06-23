# 可用的像素点计算方式
import numpy as np
def CPiexls(out_file):
    from PIL import Image
    import numpy as np

    # 加载图像并将其转换为灰度模式
    image = Image.open(out_file).convert("L")  # "L"表示灰度模式

    # 将图像转换为numpy数组
    image_array = np.array(image)

    # 定义黑白的阈值
    threshold = 1  # 小于128的像素为黑色，大于等于128的像素为白色

    # 将灰度图转换为二值图像，黑色为0，白色为1
    binary_image = (image_array >= threshold).astype(int)

    # 获取图像的行数和列数
    rows, cols = image_array.shape

    # 计算每列（纵向）的黑色和白色像素总数
    black_counts = np.sum(binary_image == 0, axis=0)  # 黑色像素总数
    white_counts = np.sum(binary_image == 1, axis=0)  # 白色像素总数

    # 输出黑白像素,总数
    # print(output_file + f"总计行数: {rows}")
    # print(output_file + f"总计列数: {cols}")
    # print("每列黑色像素总数:", black_counts)
    # print("每列白色像素总数:", white_counts)

    # 对数组进行从小到大排序，并获得排序后元素的索引
    sorted_indices = np.argsort(black_counts)# 索引
    sorted_values = np.sort(black_counts) # 值

    # 将排序后的值和原始索引分开存储
    sorted_coords = sorted_indices.tolist()
    sorted_values = sorted_values.tolist()

    return sorted_coords, sorted_values,cols


# 将像素点找到与n最近的分割点
def find_nearest_segment(cols, byte, n):
    # 将cols分成byte份
    segments = np.linspace(cols / byte, cols, byte)

    # 找到与n最近的分割点
    nearest_index = np.argmin(np.abs(segments - n))

    # print(segments)
    return nearest_index + 1  # 返回n属于第几份以及所有分割点


def GetIndex(decimal_packets,out_file):
    byte = decimal_packets.shape[1]
    sorted_coords, sorted_values,cols = CPiexls(out_file)
    # 获得5个字节
    index = []

    for i in range(len(sorted_coords)):
        if len(index) >= 2:
            break
        n = find_nearest_segment(cols, byte, sorted_coords[i] + 1)
        if n not in index:
            index.append(n)
    # d = []
    # for i in range(len(sorted_coords)):
    #     d.append(find_nearest_segment(cols, byte, sorted_coords[i] + 1))
    # print(d)
#    print(sorted_coords)
#    print(sorted_values)
    return index


if __name__ == '__main__':
    in_file = "E:\cy\code\code\dataset\image\dhcp2.png"
    output_file = 'dhcp'
    out_file = "E:\cy\code\code\dataset\\result\\nyud\\" + output_file +"2.png"
    CPiexls(output_file,out_file)
