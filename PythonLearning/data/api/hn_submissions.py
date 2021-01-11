import requests

from operator import itemgetter

# 执行API调用并存储响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print('Status code: {}'.format(r.status_code))

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:10]:
    # 对每篇文章,都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/{}.json'.format(
        str(submission_id)))
    submission_r = requests.get(url)
    print(submission_r.status_code)
    reponse_dict = submission_r.json()

    submission_dict = {
        'title': reponse_dict['title'],
        'link': 'https://news.ycombinator.com/item?id={}'.format(
            str(submission_id)),
        'commemts': reponse_dict.get('descendants', 0)
        }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('commemts'),
                          reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['commemts'])
