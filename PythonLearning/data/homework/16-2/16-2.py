import csv
import matplotlib.pyplot as plt
from datetime import datetime

death_valley = "death_valley_2014.csv"
sitka = "sitka_weather_2014.csv"


def temperature(filename):
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
        return dates, highs, lows


death_valley_dates, death_valley_highs, death_valley_lows = temperature(death_valley)
sitka_dates, sitka_highs, sitka_lows = temperature(sitka)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(death_valley_dates, death_valley_highs, "r", alpha=0.5)
plt.plot(death_valley_dates, death_valley_lows, "r", alpha=0.5)
plt.plot(sitka_dates, sitka_highs, "b", alpha=0.5)
plt.plot(sitka_dates, sitka_lows, "b", alpha=0.5)
plt.fill_between(death_valley_dates, death_valley_highs, death_valley_lows, alpha=0.1, facecolor="r")
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, alpha=0.1, facecolor="b")
plt.title("Daily high and low The temperature contrast, 2014\nDeath Valley and Sitka", fontsize=12)
plt.xlabel("", fontsize=12)
plt.xticks(rotation=30)
# fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12, which="major")
plt.show()
