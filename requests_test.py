import time

import requests

if __name__ == '__main__':
    for item in range(0,100):
        proxy = 'http://{}:{}@{}:{}'.format('5552ED71', 'CEC487AA75FA', 'tunnel.qg.net', '13611')
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get("https://httpbin.org/get", proxies=proxies)
        print(response.text)
