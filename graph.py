import matplotlib.pyplot as plt

# Function to read data from file and parse it
def read_data(filename):
    with open(filename) as f:
        data = f.read().split('\n')
    data = [row for row in data if row]  # Remove empty lines
    x = [row.split(',')[0] for row in data]
    y1 = [row.split(',')[1] for row in data]
    y2 = [row.split(',')[2] for row in data]
    x.pop(0)
    y1.pop(0)
    y2.pop(0)
   
    # Convert x values to appropriate data type
    processed_x = []
    for value in x:
        if '^' in value:  # Handle power notation
            base, exponent = map(int, value.split('^'))
            processed_x.append(base ** exponent)
        else:
            processed_x.append(int(value))
   
    y1 = [float(i) for i in y1]
    y2 = [float(i) for i in y2]
    return processed_x, y1, y2

# Insertion Sort
x_insertion, y1_insertion, y2_insertion = read_data('InsertionSortResults.txt')
plt.figure()
plt.plot(x_insertion, y1_insertion, label='Process')
plt.plot(x_insertion, y2_insertion, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Insertion Sort')
plt.legend()
plt.show()

# Merge Sort
x_merge, y1_merge, y2_merge = read_data('MergeSortResults.txt')
plt.figure()
plt.plot(x_merge, y1_merge, label='Process')
plt.plot(x_merge, y2_merge, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Merge Sort')
plt.legend()
plt.show()

# Quick Sort
x_quick, y1_quick, y2_quick = read_data('QuickSortResults.txt')
plt.figure()
plt.plot(x_quick, y1_quick, label='Process')
plt.plot(x_quick, y2_quick, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Quick Sort')
plt.legend()
plt.show()

# Radix Sort
x_radix, y1_radix, y2_radix = read_data('RadixSortResults.txt')
plt.figure()
plt.plot(x_radix, y1_radix, label='Process')
plt.plot(x_radix, y2_radix, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Radix Sort')
plt.legend()
plt.show()

# Bubble Sort
x_bubble, y1_bubble, y2_bubble = read_data('BubbleSortResults.txt')
plt.figure()
plt.plot(x_bubble, y1_bubble, label='Process')
plt.plot(x_bubble, y2_bubble, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Bubble Sort')
plt.legend()
plt.show()
