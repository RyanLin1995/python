
# gen_cookies.py

import json

# 从浏览器中复制出来的 Cookie 字符串
cookie_str = "pgv_pvi=3998676992; RK=TNZUpO7mXt; ptcz=5fe26eb4ace609ffc0faf2b53fc072bdc53b53d3c77738f8df9831e26eb282ca; pgv_pvid=1111102774; rewardsn=; wxtokenkey=777; _sm_au_c=kPUx6AAb890WXsnqiOqXyiIRlmjCPA4czVqFWAlizvbQgAAAADy5C5TSpBdGCMDkTGXDeeaR3/7MGx6X7kuBM5zmV6QM=; ua_id=vspOdNz85FApmBhAAAAAAIB7aGg2aBidjAu_dKUgLL8=; pgv_si=s6403266560; uuid=9f3678db78d488ef1a4533e51c522b8d; rand_info=CAESIFJfh03vDfae+V4Of+80UO81UFz6Q+fF0odzgMncBAOW; slave_bizuin=3084694063; data_bizuin=3084694063; bizuin=3084694063; data_ticket=ZuaDgP6osB0HileU08aTSXHgb8W0EsRc+2tpCb5nUFtooOdjScGaWdpUwk9Mmg4v; slave_sid=WTNjVGhxTnpmdnNQaElpbDFXX0djSEZaaERDTmphY3pvSHpoOFJmUzRDeXBCcGpUTE1FNGNWbDVGMzFUM1VteVFnV3RNaTNEd3JWX2pJakFDSGNWRF9PMVNySjc4RFRRUUIwbm9LUDJoYWI2OHduWUVSQkY0UFZ0Z3F0NGR3ejgzbzBGVFhaU2llVFlzWkZm; slave_user=gh_835387e33c19; xid=9fe176975caf874bcc6aac651184077c; openid2ticket_oL7Lct1LkwPInEqymxzS51qsDOa8=pspCdh1rd1XiDBU+hxn3aZBjbSSM0ZNVGQo4Wi5QJBA=; mm_lang=zh_CN"

cookie = {}
# 遍历 cookie 信息
for cookies in cookie_str.split("; "):
    cookie_item = cookies.split("=")
    cookie[cookie_item[0]] = cookie_item[1]
# 将cookies写入到本地文件
with open('cookie.txt', "w") as file:
    #  写入文件
    file.write(json.dumps(cookie))