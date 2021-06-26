import os
import csv

source_folder = "csv_file"
dest_folder = "new_csv_file"
os.makedirs(dest_folder, exist_ok=True)

for file in os.listdir(source_folder):
    with open(os.path.join(source_folder, file)) as f:
        csv_file = csv.reader(f)
        header = next(csv_file)
        csv_data = list(csv_file)

    with open(os.path.join(dest_folder, file), "w", newline="") as nf:
        for data in csv_data:
            new_csv = csv.writer(nf)
            new_csv.writerow(data)