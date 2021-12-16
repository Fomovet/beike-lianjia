import time

import requests

if __name__ == '__main__':
    for item in range(0,100):
        proxy = 'http://{}:{}@{}:{}'.format('695364BB', '442DC4C7480C', 'tunnel.qg.net', '18634')
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get("https://httpbin.org/get", proxies=proxies)
        print(response.text)
