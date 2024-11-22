import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.font_manager import FontProperties

FontSize=18

def scientific_notation(number):
    """
    Converts a number to scientific notation with two decimal places,
    without rounding the mantissa.
    """
    if number == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(number))))
    mantissa = number / (10 ** exponent)
    mantissa_str = "{:.9f}".format(mantissa)  
    mantissa_str = mantissa_str[:mantissa_str.find('.')+3]  
    mantissa_str = mantissa_str.rstrip('.') 
    return f"{mantissa_str}e{exponent}"


bugs = ['Bug#1', 'Bug#3', 'Bug#4', 'Bug#5', 'Bug#9']
ethereum_blocks = [298309, 1431881, 1242520, 1499067, 1499197]
bsc_blocks = [4176, 1299852, 1338945, 1499562, 1499656]

fig, ax = plt.subplots(figsize=(8, 2.75))

bar_width = 0.35  
gap = 0.1         
index = np.arange(len(bugs))

bar_ethereum_start = index - bar_width / 2 - gap / 2
bar_bsc_start = index + bar_width / 2 + gap / 2

bar1 = ax.bar(bar_ethereum_start, ethereum_blocks, bar_width, label='Ethereum', color='#82B0D2')
bar2 = ax.bar(bar_bsc_start, bsc_blocks, bar_width, label='BSC', color='#FA7F6F')

ax.set_xlabel('Bug types', fontsize=FontSize)
ax.set_ylabel('Blocks', fontsize=FontSize)
# ax.set_title('Impact of Bugs on Ethereum and Binance Smart Chain', fontsize=16)

ax.set_xticks(index)
ax.set_xticklabels(bugs, fontsize=FontSize)
ax.yaxis.set_tick_params(labelsize=FontSize)

ax.set_yscale('log')

# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, fontsize=FontSize, frameon=False)
ax.legend(fontsize=FontSize-7)

max_value = max(max(ethereum_blocks), max(bsc_blocks))
ax.set_ylim(top=max_value + 8e6)  

def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        label = scientific_notation(height)
        font = FontProperties(family='Arial', size=FontSize-4)
        ax.annotate(label,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 0.5),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontproperties=font)

add_labels(bar1)
add_labels(bar2)

plt.tight_layout()
plt.savefig('bugs_blocks.pdf', format='pdf')
plt.show()