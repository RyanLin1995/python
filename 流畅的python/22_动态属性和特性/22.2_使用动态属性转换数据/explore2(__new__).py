from collections import abc
import keyword


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __new__(cls, arg):  # __new__ 是类方法，第一个参数是类本身，有余下的参数与 __init__ 方法一样，只是没有 self
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)  # 默认情况下是委托给超类的 __new__ 方法。这里调用的是 object 基类的 __new__ 方法，传入的参数是 FrozenJSON
        elif isinstance(arg, abc.MutableSequence):  # __new__ 余下的代码跟 explore1 中的 build 一致
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.data[k] = v

    def __getattr__(self, name):
        try:
            return getattr(self.data, name)
        except AttributeError:
            return FrozenJSON(self.data[
                                  name])  # 这里之前调用的是 FrozenJSON.build 方法，现在需要调用 FrozenJSON 类，python 将调用 FrozenJSON.__new__ 来处理该类

    def __dir__(self):
        return self.data.keys()


if __name__ == '__main__':
    import json

    # raw_feed = json.load(open('data/osconfeed.json'))
    raw_feed = {"Schedule":
                    {"conferences": [{"serial": 115}],
                     "events": [
                         {"serial": 34505,
                          "name": "Why Schools Don´t Use Open Source to Teach Programming",
                          "event_type": "40-minute conference session",
                          "time_start": "2014-07-23 11:30:00",
                          "time_stop": "2014-07-23 12:10:00",
                          "venue_serial": 1462,
                          "description": "Aside from the fact that high school programming...",
                          "website_url": "http://oscon.com/oscon2014/public/schedule/detail/34505",
                          "speakers": [157509],
                          "categories": ["Education"]}
                     ],
                     "speakers": [
                         {"serial": 157509,
                          "name": "Robert Lefkowitz",
                          "photo": None,
                          "url": "http://sharewave.com/",
                          "position": "CTO",
                          "affiliation": "Sharewave",
                          "twitter": "sharewaveteam",
                          "bio": "Robert ´r0ml´ Lefkowitz is the CTO at Sharewave, a startup..."}
                     ],
                     "venues": [
                         {"serial": 1462,
                          "name": "F151",
                          "category": "Conference Venues"}
                     ]
                     }
                }
    feed = FrozenJSON(raw_feed)
    print(feed)
    print(len(feed.Schedule.speakers))
    print(feed.keys())
    print(sorted(feed.Schedule.keys()))
    for key, value in sorted(feed.Schedule.items()):
        print(f'{len(value):3} {key}')
    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.flavor)
