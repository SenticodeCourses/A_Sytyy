import requests


def get_url(topic , key):
    subscription_key = key
    assert subscription_key

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    search_term = topic

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term,  "imageType": "photo", 'mkt': 'ru-RU'}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    img_urls = [img["contentUrl"] for img in search_results["value"][:7]]
    print(1)
    return img_urls