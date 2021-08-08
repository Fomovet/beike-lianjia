import os
import re

import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

url = 'https://sh.ke.com/xiaoqu/pudong/pg1'


def getList():
    headers = {
        "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    proxies = {'http': 'http://' + '101.132.178.61:8080'}
    r = requests.get(url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(r.content, "lxml")
    house_elems = soup.find_all('li', 'xiaoquListItem')
    os.makedirs('./image/', exist_ok=True)
    print('创建图片文件夹完毕')
    for item in house_elems:
        # 获取房源code
        housecode = item.get('data-housecode')
        # 获取房源名称
        href = item.find('a', class_='img maidian-detail').get('href')
        # 准备好房源房源详情URL
        house_url = href + '?fb_expo_id=' + housecode
        # 获取房源名称
        name = item.find('div', class_='title')
        # 获取图片
        img = item.find('img', class_='lj-lazy')
        # 将名称换行
        name = name.text.replace("\n", "")
        # 获取URL当前区
        split_url = r.url.split('/')[4]
        # 创建好区域文件夹
        os.makedirs('./image/{0}/{1}'.format(split_url, name), exist_ok=True)
        # 访问详情下载图片
        getListDetail(house_url, split_url, name)


def getListDetail(house_url, quyu_url, name):
    headers = {
        "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    proxies = {'http': 'http://' + '101.132.178.61:8080'}
    r = requests.get(house_url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(r.content, "lxml")
    find_ol = soup.find('ol')
    print(name,'总图片数量：', len(find_ol('li')), '张')
    for index, find_li in enumerate(find_ol('li')):
        # get = find_li.find('li', class_='CLICKDATA').get('data-src')
        # 切割图片水印后缀，真实图片地址
        split_img_url = find_li.get('data-src')[:-12]
        # 准备图片名称
        split_img_name = find_li.get('data-src')[:-12].split('/')[-1]
        # 将图片写入文件夹
        urlretrieve(split_img_url, './image/{0}/{1}/{2}'.format(quyu_url, name, split_img_name))
        print(name,'总图片数量:', len(find_ol('li')), '张，' + '当前正在下载', name, '第:', index + 1, '张')
        print(split_img_url, name, '第:', index + 1, '张已下载完毕')


if __name__ == '__main__':
    getList()
