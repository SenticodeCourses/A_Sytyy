from PIL import Image
import requests
from io import BytesIO


def edit_img(topic, img_urls):
    imgs = []
    for url in img_urls:
        try:
            response = requests.get(url, timeout=10)
            img = Image.open(BytesIO(response.content)).resize((600, 400))
            imgs.append(img)
        except:
            continue
    print(2)
    count = 1
    if imgs:
        for img in imgs:
            try:
                img.save(r'C:\Users\sytyy\PycharmProjects\untitled\block chain parsser\картинки\{}_{}.png'.format(count,topic))
            except:
                img.convert('RGB').save(r'C:\Users\sytyy\PycharmProjects\untitled\block chain parsser\картинки\{}_{}.png'.format(count,topic))
            count += 1
    print(3)
