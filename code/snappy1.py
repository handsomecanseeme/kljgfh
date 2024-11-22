import snappy
from web3 import Web3
import secrets
import matplotlib.pyplot as plt
import random

FontSize=18

def generate_high_entropy_data_secrets(size):
    data = secrets.token_bytes(size)
    return data

def plot_with_dual_y_axes(x, list1, list2, mark_x, xlabel="X-axis", ylabel1="List 1", ylabel2="List 2", label1="List 1", label2="List 2"):
    if len(x) != len(list1) or len(x) != len(list2):
        raise ValueError("All lists must have the same length")
    
    if mark_x in x:
        mark_index = x.index(mark_x)
    else:
        raise ValueError("mark_x not in x list")

    fig, ax1 = plt.subplots(figsize=(8, 3))

    plt.style.use('seaborn-v0_8')
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    ax1.plot(x[:-1], list1[:-1], label=label1, color=colors[0], linewidth=2)
    ax1.set_xlabel(xlabel, fontsize=FontSize)
    ax1.set_ylabel(ylabel1, color=colors[0], fontsize=FontSize)
    ax1.tick_params(axis='y', labelcolor=colors[0], labelsize=FontSize-4)
    ax1.tick_params(axis='x', labelsize=FontSize-4)
    ax1.set_ylim(0, 1.05)

    ax1.plot(mark_x, list1[mark_index], 'o', color=colors[0])
    ax1.text(mark_x+500, list1[mark_index], f'({mark_x}, {list1[mark_index]:.2f})', color=colors[0], ha='left', va='bottom',fontsize=FontSize-4)


    ax2 = ax1.twinx()
    ax2.plot(x[:-1], list2[:-1], label=label2, color=colors[1], linewidth=2, linestyle='--')
    ax2.set_ylabel(ylabel2, color=colors[1], fontsize=FontSize)
    ax2.tick_params(axis='x', labelsize=FontSize-4)
    ax2.tick_params(axis='y', labelcolor=colors[1], labelsize=FontSize-4)
    
    ax2.yaxis.set_ticks_position('right')

    ax2.set_yticks([4, 8, 12, 16])  
    ax2.set_yticklabels(['4', '8', '12', '16'])  
    ax2.set_ylim(4, 16.8)

  
    ax2.plot(mark_x, list2[mark_index], 'o', color=colors[1])
    ax2.text(mark_x-500, list2[mark_index], f'({mark_x}, {list2[mark_index]:.2f})', color=colors[1], ha='right', va='top', fontsize=FontSize-4)

    y1 = list1[mark_index]
    y2 = list2[mark_index]/16
    
    ax1.annotate(
        '', xy=(mark_x, y2-0.14), xycoords='data',
        xytext=(mark_x, y1), textcoords='data',
        arrowprops={'arrowstyle': '<->', 'color': '#c82423', 'lw': 2}
    )
    # ax1.annotate(
    #     '', xy=(mark_x, y2-0.13), xycoords='data',
    #     xytext=(mark_x, y1), textcoords='data',
    #     arrowprops={'arrowstyle': '|-|', 'color': 'red'}
    # )
    mid_y = (y1 + y2) / 2 -0.11
    ax1.text(mark_x+500, mid_y, 'Max Diff', color='#c82423', ha='left', va='center', fontsize=FontSize-4)


    fig.legend(loc='lower left', bbox_to_anchor=(0.05, 0.05), bbox_transform=ax1.transAxes, frameon=True, fontsize=FontSize-6)

    ax1.grid(False)
    ax2.grid(False)

    plt.tight_layout()
    plt.savefig('snappycost.pdf', format='pdf')
    plt.show()

def compress_and_calculate_ratio(byte_array):

    compressed_data = snappy.compress(byte_array)

    original_size = len(byte_array)
    compressed_size = len(compressed_data)

    compression_ratio = compressed_size / original_size
    
    return compression_ratio

def calculate_calldata_gas_cost(calldata):

    total_gas_cost = 0
    
    for byte in calldata:
        if byte == 0:
            total_gas_cost += 4
        else:
            total_gas_cost += 16
    
    average_gas_cost = total_gas_cost / len(calldata)

    return average_gas_cost

def replace_with_zeros(byte_array, num_zeros):
    original_length = len(byte_array)
    
    if num_zeros > original_length:
        raise ValueError("Number of zeros to replace exceeds the length of the byte array")

    new_byte_array = bytearray(byte_array)

    replace_positions = random.sample(range(original_length), num_zeros)

    for pos in replace_positions:
        new_byte_array[pos] = 0
    
    return bytes(new_byte_array)


def main():
    maxlen_calldata = 130859

    seed = generate_high_entropy_data_secrets(maxlen_calldata)

    gas_array = []
    compress_array = []
    seteps=100

    max_distince=-1
    max_index=0

    for i in range(0, maxlen_calldata, seteps):
        payload = replace_with_zeros(seed, i)
        compress_r = compress_and_calculate_ratio(payload)
        gas_r = calculate_calldata_gas_cost(payload)
        compress_array.append(compress_r)
        gas_array.append(gas_r)
        if max(max_distince,compress_r-(gas_r/16))!=max_distince:
            max_distince=compress_r-(gas_r/16)
            max_index=len(gas_array)-1
        if i%100==0:
            print(i)
        

    print(max_index, compress_array[max_index], gas_array[max_index], compress_array[max_index]-gas_array[max_index]/16)
    x_axis = list(range(0, maxlen_calldata, seteps))

    x_axis.append(67173)
    payload = replace_with_zeros(seed, 67173)
    compress_array.append(compress_and_calculate_ratio(payload))
    gas_array.append(calculate_calldata_gas_cost(payload))

    plot_with_dual_y_axes(x_axis, compress_array, gas_array, 67173, xlabel="The replacement amount of zero bytes", ylabel1="Compress ratio", ylabel2="Gas cost", label1="Compression ratio", label2="Gas cost")


if __name__ == "__main__":
    main()
