import matplotlib.pyplot as plt
import numpy as np

FontSize=18

def read_data(filename):
    dos_attack = []
    compressed = []
    baseline = []
    baseline_c=[]

    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 4:
                dos_attack.append(float(values[0]))
                compressed.append(float(values[1]))
                baseline.append(float(values[2]))
                baseline_c.append(float(values[3]))

    return dos_attack, compressed, baseline, baseline_c

def plot_data(dos_attack, compressed, baseline, baseline_compressed):
    x_values = range(0, len(dos_attack) )

    plt.figure(figsize=(8, 2.75))

    plt.plot(x_values, dos_attack, label='DoS attack', marker='o', color='#82B0D2')

    plt.plot(x_values, compressed, label='Attack (Compressed)', linestyle='--', marker='s', color='#FFBE7A')

    plt.plot(x_values, baseline, label='Baseline', linestyle=':', marker='^', color='#FA7F6F')
    
    plt.xlabel('Block number (from block #1,888,063)', fontsize=FontSize)
    plt.ylabel('Size (bytes)', fontsize=FontSize)
    plt.tick_params(axis='y', labelsize=FontSize)
    plt.tick_params(axis='x', labelsize=FontSize)
    plt.legend(fontsize=FontSize-6)

    plt.tight_layout()
    plt.savefig('dos_blocksize.pdf', format='pdf')
    plt.show()

if __name__ == "__main__":
    dos_attack, compressed, baseline, baseline_c = read_data('./dos_blocksize.txt')
    data1 = np.array(dos_attack)
    data2 = np.array(baseline)
    data3 = np.array(compressed)
    print(np.mean(data1)/np.mean(data2),np.mean(data3)/np.mean(data1))
    
    plot_data(dos_attack, compressed, baseline, baseline_c)