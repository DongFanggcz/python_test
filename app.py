from flask import Flask, render_template, request
import os
from PIL import Image
import pytesseract

app = Flask(__name__)

# tessdata_dir_config = r'--tessdata-dir "D:\produce\EnvApp\tesseract-ocr\tessdata"'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def upload():
    # 获取上传的文件
    file = request.files['image']

    # 保存文件到本地
    filename = file.filename
    file.save(filename)

    # 使用Pillow库打开图像
    image = Image.open(filename)

    # 使用Tesseract识别图像中的文本和数字
    text = pytesseract.image_to_string(image ,lang='chi_sim')

    # 删除临时文件
    os.remove(filename)

    # 返回识别结果
    return render_template('result.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
