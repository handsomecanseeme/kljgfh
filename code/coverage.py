import matplotlib.ticker as ticker
import random
import matplotlib.pyplot as plt
import numpy as np

FontSize=18

def format_sci_notation(value):
    if value == 0:
        return '0'
    else:
        return '{:.1e}'.format(value)

def read_data(filename):
    data = []
    
    with open(filename, 'r') as file:
        for line in file:
            value = float(line.strip())
            data.append(value)
    
    return data

x = np.linspace(0, 1440, 288)
y1 = read_data("coverage_auspex.txt")
y2 = read_data("coverage_fluffy.txt")

fig, ax = plt.subplots(figsize=(8, 2.5))

ax.plot(x, y1, linewidth=2, linestyle='--', label='Auspex', color='#82B0D2')
ax.plot(x, y2, linewidth=2, linestyle='-.', label='Fluffy', color='#FA7F6F')

xticks_location = [0, 240, 480, 720, 960, 1200, 1440]
ax.set_xticks(xticks_location)

ax.set_xticklabels(xticks_location, fontsize=FontSize)

ax.tick_params(axis='y', labelsize=FontSize)

formatter = ticker.ScalarFormatter(useOffset=False, useMathText=True)
formatter.set_powerlimits((-3, 3))  

ax.yaxis.set_major_formatter(formatter)

yticks_location = [0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000]

ax.set_yticks(yticks_location)
ax.set_yticklabels(['0','2e3','4e3','6e3','8e3','1e4','1.2e4','1.4e4','1.6e4'], fontsize=FontSize)

ax.set_xlabel('Time (Min)', fontsize=FontSize)
ax.set_ylabel('Code branches', fontsize=FontSize)

ax.set_xlim(0, 1440)
ax.set_ylim(0, 14500)  

ax.grid(axis='y', linestyle='--', linewidth=0.5, color='gray')

ax.legend(fontsize=FontSize-6, loc='center right')

plt.tight_layout()
plt.savefig('coverage.pdf', format='pdf')
plt.show()