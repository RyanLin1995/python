import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"
with open(filename, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, colum_header in enumerate(header_row):
    #     print(index, colum_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_data = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print("{} missing the data.".format(current_data))
        else:
            dates.append(current_data)
            highs.append(high)
            lows.append(low)

    # dates = list(map(lambda y: datetime.strptime(y[0], "%Y-%m-%d"), reader))
    # highs = list(map(lambda x: int(x[1]), reader))
    print(dates)
    print(highs)
    print(lows)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, "r", alpha=0.5)
plt.plot(dates, lows, "b", alpha=0.5)
plt.fill_between(dates, highs, lows, alpha=0.1, facecolor="g")
plt.title("Daily high and low temperatures, 2014\nDeath Valley", fontsize=12)
plt.xlabel("", fontsize=12)
plt.xticks(rotation=30)
# fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12, which="major")
plt.show()
