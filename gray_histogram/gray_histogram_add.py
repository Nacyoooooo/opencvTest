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

    #对图片中的每个像素值增加50
    M=np.ones(img_gray.shape,np.uint8)*50 #构建矩阵

    added_img=cv2.add(img_gray,M)
    add_img_hist=cv2.calcHist([added_img],[0],None,[256],[0,256])
    add_img_BGR=cv2.cvtColor(added_img,cv2.COLOR_GRAY2BGR)
    show_image(add_img_BGR,"added image",2)
    show_histogram(add_img_hist,"added image hist",5,"m")

    #对图片中的每个像素值减去50
    subtract_img=cv2.subtract(img_gray,M)
    add_img_hist=cv2.calcHist([added_img],[0],None,[256],[0,256])#计算直方图
    subtract_img_BGR=cv2.cvtColor(subtract_img,cv2.COLOR_GRAY2BGR)
    show_image(subtract_img_BGR,"subtract image",3)
    show_histogram(add_img_hist,"subtract image hist",6,"m")

    plt.show()

if __name__ == '__main__':
    main()