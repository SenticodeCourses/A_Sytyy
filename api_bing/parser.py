from json_bing import get_url
from edit_img import edit_img


key = KEY
topics = [topic.strip() for topic in open('topic.txt')]

for topic in topics:
    img_urls = get_url(topic, key)
    edit_img(topic, img_urls)
    break


