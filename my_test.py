import datetime
import os
import time
from urllib.request import urlretrieve
from multiprocessing.dummy import Pool as ThreadPool
url = [
    "https://ke-image.ljcdn.com/hdic-resblock/45516801-15b3-44cc-ac3d-6727a2dd685a.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/70a48725-897e-4935-9d6c-95af663bc113.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/82cff6c0-6501-4786-80c9-4327441a6274.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/c29ecd5c-88d9-4683-aafd-a448bd31a9b5.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/802bb21e-e4b1-468f-babe-d1d0fc06ce0d.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/554ec339-e823-45a6-b0d9-814f3775aae6.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/2f7ad776-31d7-461d-8254-2c7ef2bfc5be.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/b6f0adde-a714-49db-84b2-b7d237b1f959.JPG",
    "https://img.ljcdn.com/element-library/prod-3186ca31-9ed1-422e-a9bd-7a1ebc0ed767.png",
    "https://ke-image.ljcdn.com/hdic-resblock/be364798-839a-4184-a3b7-b96961ad9ff9.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/6a6de5f4-761b-4b72-9959-95b017488940.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/108b6b9c-155c-43da-9b75-0cfcf6d0520f.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/51a95ef5-80ff-44da-8203-ae1f57b35722.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/c92fa6c2-a72b-4d5c-bad2-d294d61ae211.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/c8bef06a-d02e-46aa-852b-fb473fcb5c49.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/d162871f-a9e1-4bb1-95c4-4b41b2613b4d.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/9070df9a-01c3-4752-8329-3bb95030e4a0.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/f85a8c63-5a90-40f9-af21-ce7096da129d.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/45516801-15b3-44cc-ac3d-6727a2dd685a.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/70a48725-897e-4935-9d6c-95af663bc113.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/82cff6c0-6501-4786-80c9-4327441a6274.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/c29ecd5c-88d9-4683-aafd-a448bd31a9b5.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/802bb21e-e4b1-468f-babe-d1d0fc06ce0d.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/554ec339-e823-45a6-b0d9-814f3775aae6.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/2f7ad776-31d7-461d-8254-2c7ef2bfc5be.JPG",
    "https://ke-image.ljcdn.com/hdic-resblock/b6f0adde-a714-49db-84b2-b7d237b1f959.JPG",
    "https://img.ljcdn.com/element-library/prod-3186ca31-9ed1-422e-a9bd-7a1ebc0ed767.png",
    "https://ke-image.ljcdn.com/hdic-resblock/be364798-839a-4184-a3b7-b96961ad9ff9.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/6a6de5f4-761b-4b72-9959-95b017488940.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/108b6b9c-155c-43da-9b75-0cfcf6d0520f.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/51a95ef5-80ff-44da-8203-ae1f57b35722.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/c92fa6c2-a72b-4d5c-bad2-d294d61ae211.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/c8bef06a-d02e-46aa-852b-fb473fcb5c49.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/d162871f-a9e1-4bb1-95c4-4b41b2613b4d.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/9070df9a-01c3-4752-8329-3bb95030e4a0.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/f85a8c63-5a90-40f9-af21-ce7096da129d.jpg",
    "https://ke-image.ljcdn.com/hdic-resblock/dcbe35d1-8797-474b-8163-6193f0780b7f.jpg"
]


def down(url):
    print('正在下载 : ', url)
    urlretrieve(url, './image/{0}'.format(url.split('/')[-1]))


def threes():
    pool = ThreadPool(5)
    # task and handles to pool
    ret = pool.map(down, url)
    pool.close()
    pool.join()

if __name__ == '__main__':
    # 创建好区域文件夹
    os.makedirs('./image', exist_ok=True)
    start = time.time()
    for item in url:
        threes()
    end = time.time()
    print(end - start,'秒')
