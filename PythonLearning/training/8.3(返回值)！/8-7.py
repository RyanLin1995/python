#coding:gbk
def make_album(singer,album,year=''):
    cd_name = {'name':singer,'cd':album}
    if year:
        cd_name['year'] = year
    return cd_name

cd_1 = make_album('周杰伦','晴天',2019)
print(cd_1)

cd_2 = make_album('周深','愿得一心人')
print(cd_2)

cd_3 = make_album('柏松','愿世界美好与你环环相扣')
print(cd_3)
