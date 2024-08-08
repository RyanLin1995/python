from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
def h(request):
    return "Hello, world"


app.start(port=8080, host="0.0.0.0")  # host is optional, defaults to 127.0.0.1
