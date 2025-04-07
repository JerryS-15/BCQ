import csv

file_path = "./buffer_data/wandb_0407_dqn_128.csv"
threshold = 18

total_rows = 0
over_threshold = 0

with open(file_path, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)
    # print("Headers:", headers)
    for row in reader:
        total_rows += 1
        value = float(row[1])
        if value > threshold:
            over_threshold += 1

print(f"Total number of episodes with rewards > {threshold} is: {over_threshold}/{total_rows} ({over_threshold/total_rows:.2%})")
