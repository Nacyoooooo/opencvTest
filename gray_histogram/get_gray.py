import numpy as np
import cv2 as cv
import io
from typing import TypeVar, Generic
import json
from django.shortcuts import render
from matplotlib import pyplot as plt
from django import forms

T=TypeVar('T')


class Result:
    def __init__(self,
                 code:int,
                 msg:str,
                 data:T):
        self.code=code
        self.msg=msg
        self.data=data

    @classmethod
    def ok(cls, data):
        return Result(200, "操作成功", data=data)

    @classmethod
    def fail(cls, msg):
        return Result(400, msg, data=None)

    def to_json(self):
        d=self.data
        if isinstance(self.data, np.ndarray):
            # 如果对象是 ndarray，返回其列表表示
            d=self.data.tolist()
        return json.dumps({
            'code': self.code,
            'msg': self.msg,
            'data': d
        })

def get_gray_data(image_data):
    image_stream = io.BytesIO(image_data)
    img = cv.imdecode(np.frombuffer(image_stream.getvalue(), np.uint8), cv.IMREAD_GRAYSCALE)
    # img = cv.imread('gdut.jpg', 0)
    equ = cv.equalizeHist(img)
    hist, bins = np.histogram(equ.flatten(), 256, [0, 256])
    return hist

def get_gray(image_file):
    # 使用 JpegImageFile 的 file 属性来获取原始文件对象
    with image_file.file as f:
        image_stream = io.BytesIO(f.read())  # 创建一个字节流

    # 使用 OpenCV 的 imdecode 函数从字节流中解码图像
    img = cv.imdecode(np.frombuffer(image_stream.getvalue(), np.uint8), cv.IMREAD_GRAYSCALE)

    # 如果 img 是 None，表示图像解码失败
    if img is None:
        return Result.fail("图像解码失败")

    # 继续你的图像处理逻辑...
    equ = cv.equalizeHist(img)
    hist, bins = np.histogram(equ.flatten(), 256, [0, 256])
    return Result.ok(hist)


# def main():
#     result=Result.ok('s')
#     print(result.data)
#
# if __name__ == '__main__':
#     main()

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
class ImageUploadForm(forms.Form):
    image = forms.ImageField()
@csrf_exempt  # 如果你使用 CSRF 保护，确保你的视图是安全的
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            result = get_gray(image_file)
            # 返回响应
            return HttpResponse(result.to_json(), content_type='application/json')  # 返回纯文本响应
        else:
            return HttpResponse(Result.fail("图片上传不正确").to_json())

    else:
        return HttpResponse(Result.fail("需要为post请求").to_json())