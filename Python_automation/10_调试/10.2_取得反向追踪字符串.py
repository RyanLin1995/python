import traceback

try:
    raise Exception("This is a test error")

except:
    err_file = open("err_file.txt", "a")
    err_file.write(traceback.format_exc())
    err_file.close()