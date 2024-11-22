import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Arial'
Fontsize = 18

def read_data(filename):
    data = []

    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 1:
                data.append(float(values[0]))

    return data

Waittime_before = read_data("doswaittime_before.txt")
Waittime_after = read_data("doswaittime_after.txt")

print(len(Waittime_before),len(Waittime_after))

data1 = np.array(Waittime_before)

median1 = np.median(data1)

data2 = np.array(Waittime_after)

median2 = np.median(data2)
print(median1,median2)
print(np.mean(data1),np.mean(data2))

fig, ax = plt.subplots(figsize=(8, 2.75))

bins = np.linspace(0, 150, 25)  
ax.hist(Waittime_before, bins=bins, alpha=0.5, label='Baseline', color='#82B0D2')
ax.hist(Waittime_after, bins=bins, alpha=0.5, label='DoS attack', color='#FA7F6F')

plt.xlim(-2, 150)
ax.set_xlabel('Transaction wait time (s)',fontsize=Fontsize)
ax.set_ylabel('Transaction amount',fontsize=Fontsize)
ax.legend(fontsize=Fontsize-6)

# Adding boxplot
# Inset axes for the boxplot, positioned at the top of the main axes
ax_box = ax.inset_axes([0, 1.05, 1, 0.15])

# Boxplot for Waittime_before
bp1 = ax_box.boxplot(Waittime_before, positions=[1], vert=False, patch_artist=True,
                     medianprops=dict(color='black', linewidth=5),
                     boxprops=dict(facecolor='#82B0D2', color='#82B0D2', linewidth=10, alpha=0.5),
                     )
for cap in bp1['caps']:
    # cap.set_linewidth(2)
    # cap.set_marker("_")
    # cap.set_markersize(100) 
    cap.set( ydata=cap.get_ydata() + (-0.25,+0.25))

# Boxplot for Waittime_after
bp2 = ax_box.boxplot(Waittime_after, positions=[2], vert=False, patch_artist=True,
                     medianprops=dict(color='black', linewidth=5),
                     boxprops=dict(facecolor='#FA7F6F', color='#FA7F6F', linewidth=10, alpha=0.5),
                     )

for cap in bp2['caps']:
    # cap.set_linewidth(2)
    # cap.set_marker("_")  
    # cap.set_markersize(100)  
    cap.set( ydata=cap.get_ydata() + (-0.25,+0.25))

ax_box.set_yticklabels(['', ''])
ax_box.set_xticks([])  
ax_box.set_yticks([])  
ax_box.set_xlim(ax.get_xlim()) 

for spine in ax_box.spines.values():
    spine.set_visible(False)
plt.tick_params(axis='y', labelsize=Fontsize)
plt.tick_params(axis='x', labelsize=Fontsize)


plt.tight_layout()
plt.savefig('dos_waittime.pdf', format='pdf')
plt.show()