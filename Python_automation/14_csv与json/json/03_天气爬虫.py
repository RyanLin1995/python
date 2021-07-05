import requests

location = input("Please input the location(comma): ")
location = location.split(",")
api = "f853673b99c3de8374cf2e6404138b81"

for i in location:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={i}&appid={api}"
    ret = requests.get(url)
    if ret.status_code == 200:
        with open("weather.txt", "w") as f:
            f.write(str(ret.json()))
