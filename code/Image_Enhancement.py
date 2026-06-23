import cv2
import numpy as np

def image_enhancement(current_edterout_file, current_enhance_file):
    # edterpath = "E:\cy\\files\\24_10_14\\result\\" + output_file + ".png"
    # 读取灰度图像
    edterimage = cv2.imread(current_edterout_file, cv2.IMREAD_GRAYSCALE)

    # 直方图均衡化
    equalized_image = cv2.equalizeHist(edterimage)

    # 伽玛校正
    gamma = 1.5  # 调整此值以改变亮度
    gamma_corrected = np.power(equalized_image / 255.0, gamma) * 255
    gamma_corrected = np.uint8(gamma_corrected)

    # 显示结果
    # cv2.imshow('Original Image', edterimage)
    #
    # cv2.imshow('Equalized Image', equalized_image)
    # cv2.imshow('Gamma Corrected Image', gamma_corrected)

    resized_image = cv2.resize(gamma_corrected, (640, 480))
    # savepath = "E:\cy\\files\\24_10_14\\enhancement\\" + output_file + ".png"
    cv2.imwrite(current_enhance_file, resized_image)

#    cv2.waitKey(0)
#    cv2.destroyAllWindows()



if __name__ == '__main__':
    d = ["dhcp", "gh0st", "dns", "nbns", "modbus"]
    for i in d:
        image_enhancement(i)
