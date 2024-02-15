# 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 方法，显示图片
def show_image(image,title,pos):
    # 顺序转换: BGR TO RGB
    image_RGB=image[:,:,::-1]
    #显示标题
    plt.title(title)
    plt.subplot(2,3,pos)
    plt.imshow(image_RGB)
#显示图片的灰度直方图
def show_histogram(hist,title , pos ,color):
    #显示标题
    plt.title(title)
    plt.subplot(2,3,pos)
    plt.xlabel("Bins")#横轴信息
    plt.ylabel("Pixels")#纵轴信息
    plt.xlim([0,256])#横轴范围
    plt.plot(hist,color=color)#绘制直方图
#主函数main()
def main():
    #创建画布
    plt.figure(figsize=(15,6))#画布大小
    plt.suptitle("Gray Image Histogram",fontsize=14,fontweight="bold")#设置标题形式

    #加载图片
    img=cv2.imread("children.jpg")

    #灰度转换
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #计算灰度图的直方图
    hist_img=cv2.calcHist([img_gray],[0],None,[256],[0,256])

    #展示灰度直方图
    #灰度图转换成BGR格式
    img_BGR=cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)
    show_image(img_BGR,"BGR image",1)
    show_histogram(hist_img,"gary histogram",4,"m")

    # 创建一个空数组来存储每个灰度级的像素个数
    pixel_counts = [0] * 256

    # 遍历直方图，填充 pixel_counts 数组
    for i in range(256):
        pixel_counts[i] = hist_img[i]  # 修正这里

    # 打印每个灰度级的像素个数
    print("Pixel counts for each gray level:")
    for gray_level, count in enumerate(pixel_counts):
        print(gray_level,":",count)
    plt.show()

if __name__ == '__main__':
    main()