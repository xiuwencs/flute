import random
from scapy.all import rdpcap, wrpcap
import os

from Import_hex import import_file
def newfolder(dest, new_folder):
    # 创建分割pcap文件完整路径
    new_file = os.path.join(dest, new_folder)
    # 创建文件夹
    os.makedirs(new_file, exist_ok=True)
    return new_file

def slippcap(pcapng_file, split_pcap_file, pic_num):
    # 读取原始 pcap 文件
    num = 100
    packets = rdpcap(pcapng_file)
    # num = int(len(packets) * 0.4)
    for j in range(pic_num):
        splits = []
        for i in range(num):
            # 随机抽取 num 条数据
            splits.append(packets[random.randint(0, len(packets) - 1)])
        file = split_pcap_file + "/" + str(j + 1) + ".pcapng"
        # 写入新的 pcap 文件
        wrpcap(file, splits)
    print("已生成", pic_num, "份随机数据,每份数据大小为", num)


def codde(p):
    # 获取当前脚本文件所在目录
    current_dir = os.path.dirname(os.path.abspath   (__file__))
    # 上一级目录
    parent_dir = os.path.dirname(current_dir)

    # 拼接上级目录下的 data、result
    pathin = os.path.join(parent_dir, "data/")
    pathout = "result/"
    # 分割协议，分成pic_num份
    pic_num = 1
    output_file = p
    pcapng_file = pathin + output_file + ".pcapng"
    outfile_dest = pathout + output_file

    # 在result文件夹下创建slip_pcapng_file文件夹,对数据进行分割
    split_pcap_file = newfolder(outfile_dest, 'slip_pcapng_file')
    slippcap(pcapng_file, split_pcap_file,pic_num)

    # 在result文件夹下创建trans_file文件夹,Original_image_file文件夹,
    trans_excel_file = newfolder(outfile_dest, 'trans_file')
    Original_image_file = newfolder(outfile_dest, 'Original_image_file')

    # +++++++++++++++++++++++
    # 在result文件夹下创建edterout_file文件夹,enhance_file文件夹,netplier_file文件夹
    Edterout_file = newfolder(outfile_dest, 'Edterout_file')
    enhance_file = newfolder(outfile_dest, 'enhance_file')
    netplier_file = newfolder(outfile_dest, 'netplier_file')

    # 对分割完成的数据生成Original_image
    for j in range(pic_num):
        current_pcapng_file = split_pcap_file + "/" + str(j + 1) + ".pcapng"
        trans_file = trans_excel_file + "/" + str(j + 1) + ".xlsx"
        Original_image = Original_image_file + "/" + str(j + 1) + ".png"

##        # 导入数据
        import_data = import_file(current_pcapng_file, trans_file, output_file)

        current_data = []
        for k in range(len(import_data)):  # 1357,1358
            current_data.append(import_data[k])

        from ImageEdgeDetection import edge_detection
        decimal_packets = edge_detection(output_file, current_data, Original_image)
        # print(decimal_packets.shape)
    print(output_file, "数据已完成初始图像生成")

    print(output_file, "正在进行图像处理")
    # 将Original_image_file放入DiffusionEdge算法后输出图片的过程
    from Call_Code import Diffu_Edge
    Diffu_Edge(pathout, output_file)
    print(output_file, "已完成图像处理")
    # print(Original_image_file)# result/nbns/Original_image_file
    # print(Edterout_file)# result/nbns/Edterout_file

    #    通过netplier获取关键字信息
#    print(output_file, "正在进行netplier关键字识别")
#    from Call_Code import Netplier_result
#    #    Netplier_result(pic_num, pathout, output_file)
#    print(output_file, "已完成netplier关键字识别")
#    netplierall_file = netplier_file + "/msa_fields_visual.txt"
#    netplierindex_file = netplier_file + "/save_index.txt"
#    index = []
#    with open(netplierindex_file, 'r') as file:
#        # 读取第一行并去掉行尾的换行符
#        first_line = file.readline().strip()
#        index = [int(first_line)]
#    from netplier_result import find_key
#    key_index = find_key(index, netplierall_file)
#    key_index = 2
#     print(output_file, "关键字在字节：", key_index)



    # 在分割完协议，生成Original_image后，对每个协议进行处理集成处理
    bostnum = 30# 集成次数30
    pcapnum = 50# 一次集成所需pcap文件50
    count_key = {}# 统计每次集成后所选取的关键字
    count_pro = {}  # 统计每次集成后所选取的关键字的概率
    save = []# 存储每次集成对应的图片id
    for bn in range(bostnum):
        all_index = []
        all_entropy = []
        all_entropy_nor = []
        savabn = []
        for i in range(pcapnum):
            random_number = random.randint(1, pic_num)
            savabn.append(random_number)
            current_pcapng_file = split_pcap_file + "/" + str(random_number) + ".pcapng"
            trans_file = trans_excel_file + "/" + str(random_number) + ".xlsx"
            Original_image = Original_image_file + "/" + str(random_number) + ".png"
            current_edterout_file = "result/" + output_file + "/Edterout_file/" + str(random_number) + ".png"
            current_enhance_file = enhance_file + "/" + str(random_number) + ".png"

            # 导入数据
            import_data = import_file(current_pcapng_file, trans_file, output_file)

            current_data = []
            for k in range(len(import_data)):  # 1357,1358
                current_data.append(import_data[k])

            from ImageEdgeDetection import edge_detection
            decimal_packets = edge_detection(output_file, current_data, Original_image)
            # print(decimal_packets.shape)
            from Image_Enhancement import image_enhancement
            image_enhancement(current_edterout_file, current_enhance_file)

            from CalculatePixels import GetIndex
            index = GetIndex(decimal_packets, current_enhance_file)
#            print(output_file, "的边缘分割结果是", index)

            from PixelsValue import calculate1
            entropy_jian, entropy_nor = calculate1(current_data, index)
#            print(output_file, "的熵值是", entropy_jian)

            all_index.append(index)
            all_entropy.append(entropy_jian)
            all_entropy_nor.append(entropy_nor)
        # print("第", bn,"次集成结束")
        # print(all_index)
        # print(all_entropy)
        from Probability import Probability
        prob = Probability(pcapnum, output_file, all_index, all_entropy, all_entropy_nor)
        max_key = max(prob, key=prob.get)
        max_value = prob[max_key]
        print("第", bn + 1,"次集成结束,分割点在：", max_key, "出现概率为", max_value / pcapnum)
        
        if max_key not in count_key:
            count_key[max_key] = 1
        else:
            count_key[max_key] += 1
        
        if max_key not in count_pro:
            count_pro[max_key] = max_value / pcapnum
        else:
            count_pro[max_key] += max_value / pcapnum
        
        save.append(savabn)
    savepath = pathout + output_file + "/save.txt"
    with open(savepath, 'w') as file:
        for row in save:
            # 将二维数组中的每一行转换为一个字符串，并使用空格或逗号分隔元素
            # 然后写入文件，并在每行末尾添加一个换行符
            file.write(' '.join(map(str, row)) + '\n')
#    print("分割点出现次数：", count_key)
#    print("分割点概率：", count_pro)

    final_count = {}
    for index in count_key:
#        print(index,"出现的概率为：",count_pro[index]/count_key[index])
        final_count[index] = count_pro[index] / count_key[index]
    max_key = max(count_key, key=count_key.get)
    max_value = final_count[max_key]
    print("最终分割点为：", max_key, "出现概率为", max_value)



if __name__ == '__main__':
    # pathin = input('请输入文件路径：')
    # pathout = input('请输入输出文件路径：')
    # p = input("请输出协议名称：")
    d = ["dhcp", "dns", "gh0st", "modbus", "nbns"]
#    for i in range(10):
#        print(i)
#        for p in d:
#            codde(p)
    codde("modbus")

    

