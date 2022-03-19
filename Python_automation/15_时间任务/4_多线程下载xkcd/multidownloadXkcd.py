import os
import threading
import requests

import bs4


def download_xckd(start, end):
    for url_number in range(start, end):
        # Download the page
        print(f'Downloading page http://xkcd.com/{url_number}...')
        res = requests.get(f'http://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image
        comic_elem = soup.select('#comic img')

        if not comic_elem:
            print('Could not find comic image.')

        else:
            comic_url = f"http:{comic_elem[0].get('src')}"

            # Download the image
            print(f'Downloading image {comic_url}...')
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./download
            image_file = open(os.path.join('download', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


if __name__ == '__main__':

    # Create and start the Thread objects
    download_threads = []  # a list of all the Thread objects, for check if the thread is alive
    for i in range(0, 100, 10):  # create 10 threads
        # 步长问题说明：
        # 如果把第一个线程的起始值设置为0，那么第一个迭代的值为10，第二个为20，以此类推。
        # 将 i 传入函数，则每个线程的起始值都是不同的。，第一个迭代区间为0， 10， 第二个迭代区间为10， 20，以此类推。
        download_thread = threading.Thread(target=download_xckd, args=(i, i + 10))
        download_threads.append(download_thread)
        download_thread.start()

    for download_thread in download_threads:
        download_thread.join()  # wait for all the threads to finish, the join() method is a blocking call,
        # it can wait for the thread to finish, if the thread is not alive, it will return immediately

    print('Done.')

