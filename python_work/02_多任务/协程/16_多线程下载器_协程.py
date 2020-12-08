from urllib.request import urlopen
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(file_name, url):

    req = urlopen(url)
    data = req.read()

    with open(file_name, 'wb') as f:
        f.write(data)


def main():

    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", 'https://i0.hdslb.com/bfs/archive/6c8f8952e733cdd4d9a09da8efb93b2fab697c9c.jpg'),
        gevent.spawn(downloader, "2.jpg", 'https://i1.hdslb.com/bfs/archive/32c2f0de6e28a221b67d4ef96508ad7373f057a0.jpg')
    ])


if __name__ == '__main__':
    main()
