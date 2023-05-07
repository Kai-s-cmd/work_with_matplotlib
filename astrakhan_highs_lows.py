import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/Astrakhan.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    dates, avg = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            a = int(row[3])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            avg.append(a)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, avg, c='red', alpha=0.5)

# Format plot.
plt.title('Daily avg temperatures 1881 - 2021\nAstrakhan', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig("astrakhan_graph.png")