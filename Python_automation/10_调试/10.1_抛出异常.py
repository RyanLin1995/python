def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")

    if width <= 2:
        raise Exception("Width must be greater than 2.")

    if height <= 2:
        raise Exception("Height must be greater than 2.")

    print(symbol*width)
    for i in range(height - 2):
        print(symbol + (" "*(width-2)) + symbol)
    print(symbol*width)


for sym, w, h in [("0", 3, 3), ("*", 1, 3), ("ZZ", 2, 3)]:
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print(err)
